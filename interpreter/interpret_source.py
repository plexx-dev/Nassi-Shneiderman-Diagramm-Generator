import logging
from os import remove
import re
from re import split
from typing import List, Match, Tuple

from errors.custom import InterpreterException, JavaSyntaxError, ScopeNotFoundException
from draw.Iinstruction import *

logging.warning("""Because the Interpreter is still WIP, some Java language features are not supported. These include:
    *else if statements
    *for loops
Please remove these features from the source code as they will result in incorrect behaviour""")

class Function_scope(Iterable):
    def __init__(self, child_instructions: List[Iinstruction], name: str, return_type: str, args: List[str]) -> None:
        self.contents = child_instructions
        self.name = name
        self.return_type = return_type
        self.args = args

    def __iter__(self):
        return self.contents.__iter__()

COMMENT_PATTERN = re.compile(r"""^//|^/\*\*|^\*|^--""")
REMOVE_KEYWORDS = [' ', ';', "public", "private", "final", "protected"]
VARIABLE_TAGS = ["byte", "short", "int", "long", "float", "double", "boolean", "char", "String"]
FUNCTION_IDENTIFIERS = ["void"]
FUNCTION_IDENTIFIERS.extend(VARIABLE_TAGS)

WHILE_TAG = "solange " #german for 'while'. Change this depending on your language

REPLACE = dict((re.escape(k), '') for k in REMOVE_KEYWORDS)
remove_pattern = re.compile("|".join(REPLACE.keys()))

variable_regex = "^("
for kw in VARIABLE_TAGS:
    variable_regex += fr"""{kw}|"""
variable_pattern = re.compile(variable_regex[0:-1]+")(.*=|.*;)(.*)")
print(variable_pattern)

function_regex = "^("
for kw in FUNCTION_IDENTIFIERS:
    function_regex += fr"""{kw}|"""
function_regex = function_regex[0:-1]+ ").*([(].*[)].*)"

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

def handle_variable(line:str, src: List[str], i: int) -> Tuple[Iinstruction, int]:
    groups = variable_pattern.match(line).groups()
    var_type = groups[0]
    var_name = groups[1][:-1]
    var_value = groups[2]
    if var_value == "":
        return generic_instruction(f"declare variable '{var_name}' of type {var_type}"), i
    return generic_instruction(f"declare variable '{var_name}' of type {var_type} with value {var_value}"), i


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

    elif variable_pattern.match(line):
        logging.debug("Found variable in line %i", i+1)
        return handle_variable(line, src, i)
    
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

def get_function_info(match: Match[str], line: str) -> Tuple[str, str, str]:
    groups = match.groups()
    ftype = groups[0]
    fargs = groups[1]
    fname = line.removeprefix(ftype).removesuffix(fargs) #remove return type and argument list to get the function name
    return ftype, fname, fargs

def get_function_scopes(src: List[str]) -> List[Function_scope]:
    functions = []

    i = 0
    while i < len(src):
        line = src[i]
        if match:=function_pattern.match(line):
            function_return_type, function_name, function_args = get_function_info(match, line)

            brace_offset = get_scope_start_offset(src, i)
            child_instructions, i = get_instructions_in_scope(src, i+brace_offset)
            functions.append(Function_scope(child_instructions, function_name, function_return_type, function_args.split(',')))
        i+=1
    return functions

def load_scoped_instructions(filepath: str) -> List[Function_scope]:
    src = load_src(filepath)
    return get_function_scopes(src)
