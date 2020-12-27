import logging
from os import remove
import re
from typing import Callable, List, Tuple

from errors.custom import InterpreterException, JavaSyntaxError, ScopeNotFoundException
from draw.Iinstruction import *

COMMENT_REGEX = r"""^//|^#|^COMMENT|^--"""
REMOVE_KEYWORDS = [' ', "public", "private", "void", ';']

WHILE_TAG = "solange " #german for 'while'. Change this depending on your language

REPLACE = dict((re.escape(k), '') for k in REMOVE_KEYWORDS)
remove_pattern = re.compile("|".join(REPLACE.keys()))

logging.warn("""The Interpreter is WIP and cannot interpret classes or function definitions
as those do not exist in Nass-Shneidermann Diagrams. A fix is in the making
""")

def replace_all_tags(org: str):
    return remove_pattern.sub(lambda m: REPLACE[re.escape(m.group(0))], org)

def load_src(filepath: str) -> List[str]:
    lines: List[str] = []
    brace_open_count, brace_closed_count = 0,0
    try:
        with open(filepath, encoding="utf-8") as file:
            for _line in file:
                line = replace_all_tags(_line.strip())
                if line and not re.match(COMMENT_REGEX, line):
                    lines.append(line)
                if line.__contains__('{'):
                    brace_open_count += 1
                if line.__contains__('}'):
                    brace_closed_count += 1
    except:
        raise FileNotFoundError(f"File {filepath} was not found!")

    if brace_open_count != brace_closed_count:
        raise JavaSyntaxError("Number of opened braces does not match number of closed ones. Program is ill-formed!")
    
    return lines

def check_src(src: List[str], line_index: int, tag: str) -> bool:
    if line_index >= len(src):
        return False
    return src[line_index].__contains__(tag)

def check_line_start(src: List[str], line_index: int, tag: str) -> bool:
    if line_index >= len(src):
        return False
    return src[line_index].startswith(tag)

def get_next_occurence_of(src: List[str], start_idx:int, tag:str) -> int:
    """Returns the index of the next occurence of tag in src from start_idx"""
    i = start_idx
    while i < len(src):
        if check_src(src, i, tag):
            break
        i += 1
    return i

def get_scope_start_offset(src: List[str], i: int) -> int:
    if check_src(src, i, "{"):
        return 1
    elif check_src(src, i+1, "{"):
        return 2
    raise ScopeNotFoundException("Unable to find scope start. Is the program ill-formed?")

def handle_while(line: str, src: List[str], i: int) -> Tuple[Iinstruction, int]:
    bracket_idx = line.rindex(')') # throws if while contruct is illformed

    instruction_txt = line[6:bracket_idx]
    brace_offset = get_scope_start_offset(src, i)
    child_instructions, i = get_instructions_in_scope(src, i+brace_offset)
    return while_instruction_front((WHILE_TAG + instruction_txt), child_instructions), i

def handle_else(src: List[str], i: int) -> Tuple[List[Iinstruction], int]:
    brace_offset = get_scope_start_offset(src, i)
    return get_instructions_in_scope(src, i+brace_offset)

def handle_if(line: str, src: List[str], i: int) -> Tuple[Iinstruction, int]:
    bracket_idx = line.rindex(')') # throws if the contruct is illformed
    instruction_txt = line[3:bracket_idx]

    brace_offset = get_scope_start_offset(src, i)
    true_instructions, i = get_instructions_in_scope(src, i+brace_offset)

    false_instructions = None

    #check for else statements
    if check_line_start(src, i, "}else"):
        logging.debug("found else construct in line: %i", i+1)
        false_instructions, i = handle_else(src, i)
    
    elif check_line_start(src, i+1, "else"):
        logging.debug("found else construct in line: %i", i+2)
        false_instructions, i = handle_else(src, i+1)
    
    return if_instruction(instruction_txt, true_instructions, false_instructions), i

def handle_do_while(line: str, src: List[str], i: int) -> Tuple[Iinstruction, int]:
    brace_offset = get_scope_start_offset(src, i)
    child_instructions, i = get_instructions_in_scope(src, i+brace_offset)

    instruction_txt = None
    if check_line_start(src, i, "}while("):
        end_line = src[i]
        bracket_index = end_line.rindex(')') #throws if contruct id ill-formed
        instruction_txt = end_line[7:bracket_index]
    elif check_line_start(src, i+1, "while("):
        i += 1
        end_line = src[i]
        bracket_index = end_line.rindex(')')
        instruction_txt = end_line[6:bracket_index]
    else:
        raise JavaSyntaxError("Ill-formed do-while construct!")

    return while_instruction_back(instruction_txt, child_instructions), i

def handle_instruction(line: str, src: List[str], i: int) -> Tuple[Iinstruction, int]:
    if line.startswith("while("):
        logging.debug("Found while construct in line: %i", i+1)
        return handle_while(line, src, i)
    
    elif line.startswith("if("):
        logging.debug("Found if construct in line: %i", i+1)
        return handle_if(line, src, i)

    elif line.startswith("do"):
        logging.debug("Found do-while construct in line: %i", i+1)
        return handle_do_while(line, src, i)
    
    else:
        logging.debug("found generic instruction in line %i", i+1)
        return generic_instruction(line), i

def get_instructions_in_scope(src: List[str], start_idx: int = 0) -> Tuple[List[Iinstruction], int]:
    outer_scope: List[Iinstruction] = []
    i = start_idx
    while i < len(src):

        line = src[i]
        try:
            if check_src(src, i, "}"): #We exited this scope, return it
                break

            instruction, i = handle_instruction(line, src, i)
            outer_scope.append(instruction)
            
        except Exception as e:
            logging.error("Encountered error in line %i: %s", i+1, str(e))
            raise
        except:
            logging.fatal("Encountered unexpected error in line: %i", i+1)
            raise
        i += 1
    
    return outer_scope, i

def load_instructions(filepath: str) -> List[Iinstruction]:
    src = load_src(filepath)
    instructions, i = get_instructions_in_scope(src)
    if i != len(src):
        raise InterpreterException("Unknown error during source interpretation! Unsupported language constructs or ill-formed source?")
    return instructions