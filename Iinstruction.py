import code_to_image as cti
from typing import Iterable, List
from abc import abstractmethod

from code_to_image import NSD_init, NSD_save


class Iinstruction:
    """Base class for all instructions"""

    def __init__(self, instruction_text: str) -> None:
        self.instruction_text = instruction_text

    @abstractmethod
    def to_image(self, x:float, y:float, x_sz: float, y_sz: float) -> Iterable[float]:
        pass


class generic_instruction(Iinstruction):
    """Any instruction that is not a control structure"""

    def __init__(self, instruction_text: str) -> None:
        Iinstruction.__init__(self, instruction_text)

    def to_image(self, x:int, y:int, x_sz: int, y_sz: int) -> Iterable[float]:
        new_x, new_y = cti.draw_generic_instruction(self.instruction_text, x, y, x_sz, y_sz)
        return new_x, new_y



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
    
    def to_image(self, x:int, y:int, x_sz: int, y_sz: int) -> Iterable[float]:
        true_x, true_y, true_sz_x, true_sz_y, false_x, false_y, false_sz_x, false_sz_y = cti.draw_if_statement(
        self.instruction_text,
        x, y, x_sz, y_sz)

        true_blk_sz = self.draw_true_case(true_x, true_y, true_sz_x, true_sz_y)
        false_blk_sz = self.draw_false_case(false_x, false_y, false_sz_x, false_sz_y)
        blk_sz = max(true_blk_sz, false_blk_sz)
        return x, true_y + blk_sz

    def draw_true_case(self, x: float, y:float, x_sz:float, y_sz:float) -> float:
        start_y = y
        y_sz /= len(self.true_case)
        for instruction in self.true_case:
            x, y = instruction.to_image(x, y, x_sz, y_sz)
        return y - start_y

    def draw_false_case(self, x: float, y:float, x_sz:float, y_sz:float) -> float:
        start_y = y
        if self.false_case:
            y_sz /= len(self.false_case)
            for instruction in self.false_case:
                x, y = instruction.to_image(x, y, x_sz, y_sz)
        return y - start_y

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
    
    def to_image(self, x:int, y:int, x_sz: int, y_sz: int):
        children_x, children_y, children_sz_x, children_sz_y = cti.draw_while_loop_front(self.instruction_text, x, y, x_sz, y_sz)
        blk_size = self.draw_children(children_x, children_y, children_sz_x, children_sz_y)
        return x, y + blk_size

    def draw_children(self, x:float, y:float, x_sz:float, y_sz:float) -> float:
        y_sz /= len(self.child_instructions)
        for instruction in self.child_instructions:
            x, y = instruction.to_image(x, y, x_sz, y_sz)
        return y_sz



class while_instruction_back(while_instruction_front):
    def __init__(self, condition: str, instructions: List[Iinstruction]) -> None:
        while_instruction_front.__init__(self, condition, instructions)
    
    def to_image(self, x:int, y:int, x_sz: int, y_sz: int):
        children_x, children_y, children_sz_x, children_sz_y = cti.draw_while_loop_back(self.instruction_text, x, y, x_sz, y_sz)
        blk_size = self.draw_children(children_x, children_y, children_sz_x, children_sz_y)
        return x, y + blk_size

    def draw_children(self, x:float, y:float, x_sz:float, y_sz:float) -> float:
        y_sz /= len(self.child_instructions)
        for instruction in self.child_instructions:
            x, y = instruction.to_image(x, y, x_sz, y_sz)
        return y_sz
    

if __name__ == "__main__":
    """Debugging"""
    test = if_instruction("shouldNiet()", [
        generic_instruction("Niet()"),
        generic_instruction("Niet()"),
        generic_instruction("Niet()"),
        generic_instruction("Niet()"),
    ], [
        generic_instruction("hiet()"),
        generic_instruction("hiet()"),
        if_instruction("shouldNiet()", [ generic_instruction("hiet()") ], [generic_instruction("hiet()")]),
    ])
    NSD_init(500, 500)
    test.to_image(0, 0, 250, 500)
    NSD_save("Iinstruction")