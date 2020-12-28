import logging
from os import remove
import re
from typing import List, Tuple

from errors.custom import InterpreterException, JavaSyntaxError, ScopeNotFoundException
from draw.Iinstruction import *

logging.warning("""As the Interpreter is still WIP, some Java language features are not supported. These include:
    *else if statements
    *for loops
Please remove these features from the source code as they will result in incorrect behaviour""")

COMMENT_PATTERN = re.compile(r"""^//|^/\*\*|^\*|^--""")
REMOVE_KEYWORDS = [' ', "public", "private", ';']
VARIABLE_TAGS = ["byte", "short", "int", "long", "float", "double", "boolean", "char", "String"]
FUNCTION_IDENTIFIERS = ["void"]
FUNCTION_IDENTIFIERS.extend(VARIABLE_TAGS)

WHILE_TAG = "solange " #german for 'while'. Change this depending on your language

REPLACE = dict((re.escape(k), '') for k in REMOVE_KEYWORDS)
remove_pattern = re.compile("|".join(REPLACE.keys()))

variable_regex = "^("
for kw in FUNCTION_IDENTIFIERS:
    variable_regex += fr"""{kw}|"""
variable_pattern = re.compile(variable_regex[0:-1]+")$(.*)")

function_regex = "^("
for kw in FUNCTION_IDENTIFIERS:
    function_regex += fr"""{kw}|"""
function_regex = function_regex[0:-1]+ r""").*([(].*[)].*)"""

function_pattern = re.compile(function_regex)

def replace_all_tags(org: str):
    return remove_pattern.sub(lambda m: REPLACE[re.escape(m.group(0))], org)

def load_src(filepath: str) -> List[str]:
    lines: List[str] = []
    brace_open_count, brace_closed_count = 0,0
    try:
        with open(filepath, encoding="utf-8") as file:
            for _line in file:
                line = replace_all_tags(_line.strip())
                if line and not COMMENT_PATTERN.match(line):
                    lines.append(line)
                if '{' in line:
                    brace_open_count += 1
                if '}' in line:
                    brace_closed_count += 1
    except:
        raise FileNotFoundError(f"File {filepath} was not found!")

    if brace_open_count != brace_closed_count:
        raise JavaSyntaxError("Number of opened braces does not match number of closed ones. Program is ill-formed!")
    
    return lines

def check_src(src: List[str], line_index: int, tag: str) -> bool:
    if line_index >= len(src):
        return False
    return tag in src[line_index]

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

def get_scope_exit_offset(src: List[str], start_idx: int) -> int:
    i = start_idx
    while i < len(src):
        line = src[i]

        if '{' in line:
            i += get_scope_exit_offset(src, i+1)
            line = src[i+1]
        if '}' in line:
            return i - start_idx
        i += 1

    raise ScopeNotFoundException("Unable to find scope end. Is the program ill-formed?")

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
            if check_src(src, i, '}'): #We exited this scope, return it
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

def get_function_scope_spans(src: List[str]) -> List[Tuple[int, int, str]]:
    spans = []
    i = 0
    while i < len(src):
        line = src[i]
        try:

            if match:= function_pattern.match(line):
                groups = match.groups()
                function_name = line.removeprefix(groups[0]).removesuffix(groups[1])
                function_return_type = groups[0]
                function_args = groups[1][1:-1]
                brace_offset = get_scope_start_offset(src, i)
                scope_offset = get_scope_exit_offset(src, i+brace_offset)

                span = (i+brace_offset, i+brace_offset+scope_offset, function_name)

                i += scope_offset + brace_offset
                spans.append(span)

        except Exception as e:
            logging.error("encountered error in line %i : %s", i, str(e))
            raise
        i += 1

    return spans

def scope_handler(inst_info: Tuple[List[str], List[int]]) -> List[Iinstruction]:
    src = inst_info[0]
    scope_start = inst_info[1][0]
    scope_end = inst_info[1][1]
    return get_instructions_in_scope(src[scope_start: scope_end])[0]

def named_scope_handler(inst_info: Tuple[List[str], Tuple[int, int, str]]) -> Tuple[str, List[Iinstruction]]:
    src = inst_info[0]
    scope_start = inst_info[1][0]
    scope_end = inst_info[1][1]
    function_name = inst_info[1][2]
    function_instructions, _ = get_instructions_in_scope(src[scope_start: scope_end])
    return (function_name, function_instructions)

def get_instructions_in_scopes(src: List[str], scope_spans: List[Tuple[int, int, str]]) -> List[List[Iinstruction]]:
    instructions = list(map(scope_handler, [(src, span[0:2]) for span in scope_spans]))
    return instructions

def get_instructions_in_named_scopes(src: List[str], scope_spans: List[Tuple[int, int, str]]) -> List[Tuple[str, List[Iinstruction]]]:
    instructions = list(map(named_scope_handler, [(src, span) for span in scope_spans]))
    return instructions

def load_instructions(filepath: str) -> List[List[Iinstruction]]:
    src = load_src(filepath)
    scope_spans = get_function_scope_spans(src)
    instructions = get_instructions_in_scopes(src, scope_spans)
    return instructions

def load_scoped_instructions(filepath: str) -> List[Tuple[str, List[Iinstruction]]]:
    src = load_src(filepath)
    scope_spans = get_function_scope_spans(src)
    instructions = get_instructions_in_named_scopes(src, scope_spans)
    return instructions
