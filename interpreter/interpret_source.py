import logging
import re
from typing import List, Tuple

from draw.Iinstruction import *

COMMENT_REGEX = r"""^//|^#|^COMMENT|^--"""

class JavaSyntaxError(Exception):
    pass

class ScopeNotFoundException(Exception):
    pass

def load_src(filepath: str) -> List[str]:
    lines: List[str] = []
    brace_open_count, brace_closed_count = 0,0
    try:
        with open(filepath, encoding="utf-8") as file:
            for _line in file:
                line = _line.strip().replace(' ', '')
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

def get_scope_start_offset(src: List[str], start_idx: int) -> int:
    i = start_idx
    while i < len(src):
        line = src[i]
        if line.__contains__("{"):
            return i - start_idx + 1
        i += 1
    raise ScopeNotFoundException("Unable to find scope start. Is the program ill-formed?")

def get_instructions_in_scope(src: List[str], start_idx: int = 0) -> Tuple[List[Iinstruction], int]:
    outer_scope: List[Iinstruction] = []
    i = start_idx
    while i < len(src):
        line = src[i]
        try:
            if line.__contains__('}'): #We exited this scope, return it
                return outer_scope, i
            
            if line.startswith("while("):
                logging.debug("Found while instruction in line: %i", i+1)

                bracket_idx = line.rindex(')') # throws if while contruct is illformed

                instruction_txt = line[6:bracket_idx]
                brace_offset = get_scope_start_offset(src, i)
                child_instructions, i = get_instructions_in_scope(src, i+brace_offset)

                outer_scope.append(while_instruction_front(instruction_txt, child_instructions))
            
            elif line.startswith("if("):
                logging.debug("Found if instruction in line: %i", i+1)

                bracket_idx = line.rindex(')') # throws if the contruct is illformed

                instruction_txt = line[3:bracket_idx]
                brace_offset = get_scope_start_offset(src, i)
                true_instructions, i = get_instructions_in_scope(src, i+brace_offset)

                false_instructions = None
                if src[i].__contains__("else"): #if there is an else statement, check it
                    false_instructions, i = get_instructions_in_scope(src, i+2)
                
                outer_scope.append(if_instruction(instruction_txt, true_instructions, false_instructions))

            elif line.startswith("do{"):
                #construct:
                #do{
                #...
                #}while(...);
                logging.debug("Found start of do-while instruction in line: %i", i)

                brace_offset = get_scope_start_offset(src, i)
                child_instructions, i = get_instructions_in_scope(src, i+brace_offset)

                end_line = src[i]
                bracket_idx = end_line.rindex(");")
                instruction_txt = end_line[7: bracket_idx]

                outer_scope.append(while_instruction_back(instruction_txt, child_instructions))
            
            else:
                logging.debug("Found generic instruction in line: %i", i+1)
                outer_scope.append(generic_instruction(line))
        except:
            logging.error("Encountered error in line: %i", i)
            raise # rethrow
        i += 1
    return outer_scope, 0