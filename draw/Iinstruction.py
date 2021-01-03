from typing import Iterable, List
from abc import abstractmethod
from draw import code_to_image as cti

class Iinstruction:
    """Base class for all instructions"""

    def __init__(self, instruction_text: str) -> None:
        self.instruction_text = instruction_text

    @abstractmethod
    def to_image(self, x:int, y:int, x_sz: int) -> Iterable[float]:
        pass

    @abstractmethod
    def getblksize(self) -> float:
        return self._getblksize()

    @abstractmethod
    def __str__(self) -> str:
        pass

    def _getblksize(self) -> float:
        return cti.get_text_size(self.instruction_text)[1]


class generic_instruction(Iinstruction):
    """Any instruction that is not a control structure"""

    def __init__(self, instruction_text: str) -> None:
        Iinstruction.__init__(self, instruction_text)

    def to_image(self, x:int, y:int, x_sz: int) -> Iterable[float]:
        return cti.draw_generic_instruction(self.instruction_text, x, y, x_sz, self.getblksize())

    def __str__(self) -> str:
        return self.instruction_text

class if_instruction(Iinstruction):
    """Conditional structure
        NOT.
        A.
        LOOP
    """

    def __init__(self, instruction_text: str, true_case: List[Iinstruction], false_case: List[Iinstruction]=None) -> None:
        Iinstruction.__init__(self, instruction_text)
        self.true_case = true_case
        self.false_case = false_case

    def get_truesize(self) -> float:
        sz = 0.0
        for inst in self.true_case:
            sz += inst.getblksize()
        return sz

    def get_falsesize(self) -> float:
        sz = 0.0
        if self.false_case:
            for inst in self.false_case:
                sz += inst.getblksize()
        return sz

    def getblksize(self) -> float:
        return self._getblksize() + max(self.get_truesize(), self.get_falsesize())
    
    def to_image(self, x:int, y:int, x_sz: int) -> Iterable[float]:
        true_x, true_y, true_sz_x, _, false_x, false_y, false_sz_x, _ = cti.draw_if_statement(
            self.instruction_text, x, y, x_sz, self.getblksize()
        )
        self.draw_true_case(true_x, true_y, true_sz_x)
        self.draw_false_case(false_x, false_y, false_sz_x)
        blk_size = self.getblksize()
        return x, y + blk_size

    def draw_true_case(self, x: float, y:float, x_sz:float):
        for instruction in self.true_case:
            x, y = instruction.to_image(x, y, x_sz)

    def draw_false_case(self, x: float, y:float, x_sz:float):
        if self.false_case:
            for instruction in self.false_case:
                x, y = instruction.to_image(x, y, x_sz)

    def __str__(self) -> str:
        res = f"if({self.instruction_text}) {'{'}\n"
        for inst in self.true_case:
            res += '\t'+str(inst)+";\n"
        res += "}"
        if self.false_case:
            res += " else {"
            for inst in self.true_case:
                res += '\t'+str(inst)+";\n"
            res += "}"
        return res

#TODO
# class switch_instruction(Iinstruction):
#     """Switch structure"""

#     def __init__(self, instruction_text: str, cases: List[List[Iinstruction]]) -> None:
#         Iinstruction.__init__(self, instruction_text)
#         self.child_cases = cases
    
#     def to_image(self, x:int, y:int, x_sz: int, y_sz: int) -> Iterable[float]:
#         """TODO: implement"""
#         return []

#     def draw_children(self, x:float, y:float, x_sz:float, y_sz:float) -> float:
#         """TODO: implement"""
#         return 0.0



class while_instruction_front(Iinstruction):

    def __init__(self, condition: str, instructions: List[Iinstruction]) -> None:
        Iinstruction.__init__(self, condition)
        self.child_instructions = instructions

    def get_children_size(self) -> float:
        children_sz = 0
        for inst in self.child_instructions:
            children_sz += inst.getblksize()
        return children_sz

    def getblksize(self) -> float:
        return self._getblksize() + self.get_children_size()
    
    def to_image(self, x:int, y:int, x_sz: int) -> Iterable[float]:
        children_x, children_y, children_sz_x = cti.draw_while_loop_front(self.instruction_text, x, y, x_sz, self.getblksize())
        self.draw_children(children_x, children_y, children_sz_x)

        return x, y + self.getblksize()


    def draw_children(self, x:float, y:float, x_sz:float):
        for inst in self.child_instructions:
            x, y = inst.to_image(x, y, x_sz)
        return self.get_children_size()

    def __str__(self) -> str:
        res = "while(" + self.instruction_text + "){\n"
        for inst in self.child_instructions:
            res += '\t'+str(inst)+";\n"
        res += '}'
        return res


class while_instruction_back(while_instruction_front):
    def __init__(self, condition: str, instructions: List[Iinstruction]) -> None:
        while_instruction_front.__init__(self, condition, instructions)
    
    def to_image(self, x:int, y:int, x_sz: int):
        children_x, children_y, children_sz_x = cti.draw_while_loop_back(self.instruction_text, x, y, x_sz, self.getblksize())
        self.draw_children(children_x, children_y, children_sz_x)
        return x, y + self.getblksize()

    def __str__(self) -> str:
        res = "do{\n"
        for inst in self.child_instructions:
            res += '\t' +str(inst) + ";\n"
        res += f"{'}'}while({self.instruction_text});"
        return res

class for_instruction(while_instruction_front):
    pass