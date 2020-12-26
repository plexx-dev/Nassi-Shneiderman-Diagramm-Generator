import logging
from os import remove
import re
from typing import List, Text, Tuple

from draw.Iinstruction import *

COMMENT_REGEX = r"""^//|^#|^COMMENT|^--"""
REMOVE_KEYWORDS = [' ', "public", "private", "void"]

WHILE_TAG = "solange " #german for 'while'. Change this depending on your language

REPLACE = dict((re.escape(k), '') for k in REMOVE_KEYWORDS)
remove_pattern = re.compile("|".join(REPLACE.keys()))

class JavaSyntaxError(Exception):
    pass

class ScopeNotFoundException(Exception):
    pass

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

def get_next_occurence_of(src: List[str], start_idx:int, tag:str) -> int:
    i = start_idx
    while i < len(src):
        if src[i].__contains__(tag):
            return i
        i += 1

def get_scope_start_offset(src: List[str], start_idx: int) -> int:
    i = get_next_occurence_of(src, start_idx, '{')
    if i != len(src):
        return i + 1
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
                logging.debug("Found while construct in line: %i", i+1)

                bracket_idx = line.rindex(')') # throws if while contruct is illformed

                instruction_txt = line[6:bracket_idx]
                brace_offset = get_scope_start_offset(src, i)
                child_instructions, i = get_instructions_in_scope(src, i+brace_offset)

                outer_scope.append(while_instruction_front((WHILE_TAG + instruction_txt), child_instructions))
            
            elif line.startswith("if("):
                logging.debug("Found if construct in line: %i", i+1)

                bracket_idx = line.rindex(')') # throws if the contruct is illformed

                instruction_txt = line[3:bracket_idx]
                brace_offset = get_scope_start_offset(src, i)
                true_instructions, i = get_instructions_in_scope(src, i+brace_offset)

                false_instructions = None
                #if there is an else statement, check it
                if src[i].__contains__("else"):
                    logging.debug("found else construct in line: %i", i+1)
                    brace_offset = get_scope_start_offset(src, i)
                    false_instructions, i = get_instructions_in_scope(src, i+brace_offset)
                elif src[i+1].__contains__("else"):
                    logging.debug("found else construct in line: %i", i+2)
                    brace_offset = get_scope_start_offset(src, i+1)
                    false_instructions, i = get_instructions_in_scope(src, i+1+brace_offset)

                
                outer_scope.append(if_instruction(instruction_txt, true_instructions, false_instructions))

            elif line.startswith("do"):
                logging.debug("Found start of do-while construct in line: %i", i+1)

                brace_offset = get_scope_start_offset(src, i)
                child_instructions, i = get_instructions_in_scope(src, i+brace_offset)

                end_line = src[i]
                bracket_idx = end_line.rindex(");")
                instruction_txt = end_line[7: bracket_idx]

                outer_scope.append(while_instruction_back((WHILE_TAG + instruction_txt), child_instructions))
            
            else:
                logging.debug("Found generic instruction in line: %i", i+1)
                outer_scope.append(generic_instruction(line))
        except:
            logging.error("Encountered error in line: %i", i+1)
            raise # rethrow
        i += 1
    return outer_scope, 0