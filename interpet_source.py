from Iinstruction import *
import logging
import re
from typing import Any, Iterator

class Scope():

    def __init__(self, enclosing_scope) -> None:
        self.enclosing_scope = enclosing_scope
        self.contents = []
    
    def add_instruction(self, instruction) -> None:
        self.contents.append(instruction)

    def add_subscope(self, subscope) -> None:
        self.contents.append(subscope)

def load_src(filepath: str) -> list[str]:
    lines = []
    try:
        with open(filepath) as file:
            for _line in file:
                line:str = _line.strip()
                if line and not re.match(r"""^//|^#|^COMMENT|^--""", line):
                    lines.append(line)
    except:
        logging.error(f"Failed to open input file {filepath}!")
    
    return lines

def get_scopes(src: list[str]):
    global_scope = Scope(None)
    current_scope = global_scope

    for line in src:
        logging.debug(line)
        if line.__contains__('}'):
            current_scope.add_instruction("scope exit")
            current_scope = current_scope.enclosing_scope
        if line.__contains__('{'):
            current_scope.add_instruction("scope enter")
            subscope = Scope(current_scope)
            current_scope.add_subscope(subscope)
            current_scope = subscope

        elif not line.__contains__('}'):
            current_scope.add_instruction("generic instruction")
    
    return global_scope

def get_instructions(scope: Scope) -> list[Any]:
    instructions = []

    for item in scope.contents:
        if isinstance(item, Scope):
            instructions.extend(get_instructions(item))
        else:
            instructions.append(item)
    
    return instructions



def get_scoped_instructions(filepath:str) -> list[Any]:
    source_code = load_src(filepath)
    global_scope = get_scopes(source_code)

    instructions = get_instructions(global_scope)
    return instructions

if __name__ == "__main__":

    def print_scope(scope: Scope):
        print('[', end='')
        for item in scope.contents:
            if isinstance(item, Scope):
                print_scope(item)
            else:
                print(item, end=", ")
        print(']')

    logging.basicConfig(level=logging.DEBUG)
    inst = get_scoped_instructions("res/input/input.java")
    print(inst)