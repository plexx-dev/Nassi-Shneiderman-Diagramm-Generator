"""function_scope.py: #TODO"""

__author__      = "Weckyy702"

from typing import Iterable, List
from draw.Iinstruction import Iinstruction


class Function_scope(Iterable):
    def __init__(self, child_instructions: List[Iinstruction], name: str, return_type: str, args: List[str]) -> None:
        self.contents = child_instructions
        self.name = name
        self.return_type = return_type
        self.args = args

    def get_height(self) -> int:
        h = 0.0
        for inst in self.contents:
            h += inst.getblkheight()
        return int(h)

    def get_width(self) -> int:
        w = 200.0 #minimum width for every block
        for inst in self.contents:
            w = max(w, inst.getblkwidth())
        return int(w)

    def __iter__(self):
        return self.contents.__iter__()