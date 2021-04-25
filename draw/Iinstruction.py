"""Interafce for all instruction types"""

__author__ ="Weckyy702"

from abc import ABCMeta, abstractmethod
from typing import Tuple, List, Optional

from . import code_to_image as cti

class instruction(metaclass=ABCMeta):
    def __init__(self, instruction_text: str) -> None:
        self.instruction_text = instruction_text

    @abstractmethod
    def convert_to_image(self, x: int, y: int, width: int) -> int:
        pass

    @abstractmethod
    def get_block_width(self):
        return self.get_text_width()

    @abstractmethod
    def get_block_height(self):
        return self.get_text_height()



    def get_text_width(self):
        return cti.get_text_size(self.instruction_text)[0]

    def get_text_height(self):
        return cti.get_text_size(self.instruction_text)[1]



class generic_instruction(instruction):
    def __init__(self, instruction_text: str) -> None:
        super().__init__(instruction_text)

    def convert_to_image(self, x: int, y: int, width: int) -> int:
        height = self.get_block_height()
        return cti.draw_generic_instruction(self.instruction_text, x, y, width, height)

    def get_block_width(self):
        return super().get_block_width()

    def get_block_height(self):
        return super().get_block_height()



class if_instruction(instruction):
    def __init__(self, instruction_text: str, true_case: List[instruction], false_case: Optional[List[instruction]]) -> None:
        super().__init__(instruction_text)
        self.true_case = true_case
        self.false_case = false_case

    def convert_to_image(self, x: int, y: int, width: int) -> int:
        true_width = self.get_true_width()

        true_x, true_y, false_x, false_y = cti.draw_if_statement(self.instruction_text, x, y, true_width, width)

        self.draw_children(true_x, true_y, true_width, false_x, false_y, width-true_width)

        return y + self.get_block_height()

    def draw_children(self, true_x:int, true_y:int, true_width:int, false_x:int, false_y:int, false_width:int):
        for instruction in self.true_case:
            true_y = instruction.convert_to_image(true_x, true_y, true_width)

        if self.false_case:
            for instruction in self.false_case:
                false_y = instruction.convert_to_image(false_x, false_y, false_width)

    def get_block_width(self) -> int:
        text_width = self.get_text_width()
        
        true_width = self.get_true_width()
        false_width = self.get_false_width()

        return max(text_width, true_width + false_width)

    def get_block_height(self):
        text_height = self.get_text_height()
        true_height = self.get_true_height()
        false_height = self.get_false_height()
        
        return text_height + max(true_height, false_height)

    def get_text_width(self):
        return int(super().get_text_width() * 1.5)

    def get_true_width(self) -> int:
        width = 200
        for instruction in self.true_case:
            width = max(width, instruction.get_block_width())
        return width

    def get_false_width(self) -> int:
        width = 200
        if self.false_case:
            for instruction in self.false_case:
                width = max(width, instruction.get_block_width())
        return width

    def get_true_height(self) -> int:
        height = 0

        for instruction in self.true_case:
            height += instruction.get_block_height()

        return height

    def get_false_height(self) -> int:
        height = 0
        
        if self.false_case:
            for instruction in self.false_case:
                height += instruction.get_block_height()

        return height



class while_instruction_front(instruction):
    def __init__(self, condition_text: str, child_instructions: List[instruction]) -> None:
        super().__init__(condition_text)
        self.children = child_instructions

    def convert_to_image(self, x: int, y: int, width: int) -> int:
        block_height = self.get_block_height()

        children_x, children_y, children_width = cti.draw_while_loop_front(self.instruction_text, x, y, width, block_height)

        self.draw_children(children_x, children_y, children_width)

        return y + block_height

    def draw_children(self, children_x:int, children_y:int, children_width:int):
        for instruction in self.children:
            children_y = instruction.convert_to_image(children_x, children_y, children_width)

    def get_block_width(self):
        width = self.get_text_width()

        for instruction in self.children:
            width = max(width, instruction.get_block_width() / (1 - cti.BLOCK_OFFSET_RATIO)) #instructions inside a bock take up more space, so compensate for that

        return int(width)

    def get_block_height(self):
        height = self.get_text_height()

        for instruction in self.children:
            height += instruction.get_block_height()

        return height

class while_instruction_back(while_instruction_front):
    def __init__(self, condition_text: str, child_instructions: List[instruction]) -> None:
        super().__init__(condition_text, child_instructions)

    def convert_to_image(self, x: int, y: int, width: int) -> int:
        block_height = self.get_block_height()
        children_x, children_y, children_width = cti.draw_while_loop_back(self.instruction_text, x, y, width, block_height)

        self.draw_children(children_x, children_y, children_width)

        return y + block_height



class for_instruction(while_instruction_front):
    def __init__(self, variable_text: str, condition_text: str, child_instruction: List[instruction]) -> None:
        super().__init__(condition_text, child_instruction)
        self.variable_instruction = generic_instruction(variable_text)

    def convert_to_image(self, x: int, y: int, width: int) -> int:
        y = self.variable_instruction.convert_to_image(x, y, width)
        return super().convert_to_image(x,y, width)