"""function_scope.py: Class for Function scopes"""

__author__      = "Weckyy702"

from typing import Iterable, List
from draw.Iinstruction import instruction

class Function_scope(Iterable):
    """This class serves as a container for Instructions"""

    def __init__(self, name: str, return_type: str, args: List[str]) -> None:
        self.contents = []
        self.name = name
        self.return_type = return_type
        self.args = args

    def get_height(self) -> int:
        h = 0.0
        for inst in self.contents:
            h += inst.get_block_height()
        return int(h)

    def get_width(self) -> int:
        w = 200 #minimum width for every block
        for inst in self.contents:
            w = max(w, inst.get_block_width())
        return w

    def _add_instruction(self, inst: instruction):
        self.contents.append(inst)

    def _add_instructions(self, inst: List[instruction]):
        self.contents.extend(inst)

    def __iter__(self):
        return self.contents.__iter__()