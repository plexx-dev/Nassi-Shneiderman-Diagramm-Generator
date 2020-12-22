from Iinstruction import *
import logging
import re
from typing import List, Tuple

class Scope():

    def __init__(self, enclosing_scope) -> None:
        self.enclosing_scope = enclosing_scope
        self.contents: List = []
    
    def add_instruction(self, instruction: Iinstruction) -> None:
        self.contents.append(instruction)

def load_src(filepath: str) -> List[str]:
    lines: List[str] = []
    brace_open_count, brace_closed_count = 0,0
    try:
        with open(filepath) as file:
            for _line in file:
                line = _line.strip()
                if line and not re.match(r"""^//|^#|^COMMENT|^--""", line):
                    lines.append(line)
                if line.__contains__('{'):
                    brace_open_count += 1
                if line.__contains__('}'):
                    brace_closed_count += 1
    except:
        logging.error(f"Failed to open input file {filepath}!")
    if brace_open_count != brace_closed_count:
        raise Exception("Number of opened braces does not match number of closed ones. Program is illformed!")
    
    return lines

def get_instructions_in_scope(src: List[str], start_idx: int = 0) -> Tuple[List[Iinstruction], int]:
    outer_scope = Scope(None)
    i = start_idx
    while i < len(src):
        line = src[i]
        try:
            if line.__contains__('}'): #We exited this scope, return it
                return outer_scope.contents, i
            
            if line.startswith("while("):
                logging.debug("Found while instruction in line: %i", i+1)
                bracket_idx = line.rindex(')') # throws if the while is illformed
                instruction_txt = line[6:bracket_idx]
                child_instructions, i = get_instructions_in_scope(src, i+1)
                outer_scope.add_instruction(while_instruction_front(instruction_txt, child_instructions))
            
            elif line.startswith("if("):
                logging.debug("Found if instruction in line: %i", i+1)
                bracket_idx = line.rindex(')') # throws if the contruct is illformed
                instruction_txt = line[3:bracket_idx]
                true_instructions, i = get_instructions_in_scope(src, i+2)
                false_instructions = None
                if src[i].__contains__("else"): #if there is an else statement, check it
                    false_instructions, i = get_instructions_in_scope(src, i+2)
                outer_scope.add_instruction(if_instruction(instruction_txt, true_instructions, false_instructions))
            
            else:
                logging.debug("Found generic instruction in line: %i", i+1)
                outer_scope.add_instruction(generic_instruction(line))
        except:
            logging.error("Encountered error in line: %i", i)
            raise # rethrow
        i += 1
    return outer_scope.contents, 0

if __name__ == "__main__":
    """debuging"""

    logging.basicConfig(level=logging.DEBUG)
    #inst = get_scoped_instructions("res/input/input.java")
    lines = load_src("res/input/input.java")
    global_scope = get_instructions_in_scope(lines)
    print(global_scope)