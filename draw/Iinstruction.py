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

    def __str__(self) -> str:
        return self.instruction_text



class if_instruction(instruction):
    def __init__(self, instruction_text: str, true_case: List[instruction], false_case: Optional[List[instruction]]) -> None:
        super().__init__(instruction_text)
        self.true_case = true_case
        self.false_case = false_case

    def convert_to_image(self, x: int, y: int, width: int) -> int:
        true_width = self.get_true_width()
        block_height = self.get_block_height()

        true_x, true_y, false_x, false_y = cti.draw_if_statement(self.instruction_text, x, y, true_width, width, block_height)

        self.draw_children(true_x, true_y, true_width, false_x, false_y, width-true_width)

        return y + self.get_block_height()

<<<<<<< HEAD
    def draw_children(self, true_x:int, true_y:int, true_width:int, false_x:int, false_y:int, false_width:int):
=======
    def get_truewidth(self) -> float:
        w = 50

        for inst in self.true_case:
            w = max(w, inst.getblkwidth())
        
        return w
    
    def get_falsewidth(self) -> float:
        w = 50

        if self.false_case:
            for inst in self.false_case:
                w = max(w, inst.getblkwidth())

        return w
        
    
    def to_image(self, x:int, y:int, x_sz: int) -> Iterable[float]:
        true_w = self.get_truewidth()
        false_w = self.get_falseheight()
        true_x, true_y, true_sz_x, _, false_x, false_y, false_sz_x, _ = cti.draw_if_statement(
            self.instruction_text, x, y, true_w, false_w, self.getblkheight()
        )
        self.draw_true_case(true_x, true_y, true_sz_x)
        self.draw_false_case(false_x, false_y, false_sz_x)
        blk_size = self.getblkheight()
        return x, y + blk_size

    def draw_true_case(self, x: float, y:float, x_sz:float):
>>>>>>> main
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

<<<<<<< HEAD
        return height
=======

class while_instruction_front(Iinstruction):

    def __init__(self, condition: str, instructions: List[Iinstruction]) -> None:
        Iinstruction.__init__(self, condition)
        self.child_instructions = instructions

    def get_children_height(self) -> float:
        children_sz = 0
        for inst in self.child_instructions:
            children_sz += inst.getblkheight()
        return children_sz

    def get_children_width(self) -> float:
        w = 50.0
        for inst in self.child_instructions:
            w = max(w, inst.getblkheight())
        return w

    def getblkheight(self) -> float:
        return self._getblkheight() + self.get_children_height()

    def getblkwidth(self) -> float:
        return max(self._getblkwidth(), self.get_children_width())
    
    def to_image(self, x:int, y:int, x_sz: int) -> Iterable[float]:
        children_x, children_y, children_sz_x = cti.draw_while_loop_front(self.instruction_text, x, y, x_sz, self.getblkheight())
        self.draw_children(children_x, children_y, children_sz_x)

        return x, y + self.getblkheight()


    def draw_children(self, x:float, y:float, x_sz:float):
        for inst in self.child_instructions:
            x, y = inst.to_image(x, y, x_sz)
        return self.get_children_height()
>>>>>>> main

    def __str__(self) -> str:
        res = "if\n"
        for instruction in self.true_case:
            res += '\t' + str(instruction) + '\n'

        if self.false_case:
            res += "else\n"
            for instruction in self.false_case:
                res += '\t' + str(instruction) + '\n'
        
        return res



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

    def __str__(self) -> str:
        res = "while\n"
        for instruction in self.children:
            res += '\t' + str(instruction) + '\n'
        return res

class while_instruction_back(while_instruction_front):
    def __init__(self, condition_text: str, child_instructions: List[instruction]) -> None:
        super().__init__(condition_text, child_instructions)

    def convert_to_image(self, x: int, y: int, width: int) -> int:
        block_height = self.get_block_height()
        children_x, children_y, children_width = cti.draw_while_loop_back(self.instruction_text, x, y, width, block_height)

        self.draw_children(children_x, children_y, children_width)

        return y + block_height

    def __str__(self) -> str:
        res = "do\n"
        for instruction in self.children:
            res += '\t' + str(instruction) + '\n'
        res += "while"
        return res

class for_instruction(while_instruction_front):
    def __init__(self, variable_text: str, condition_text: str, child_instruction: List[instruction]) -> None:
        super().__init__(condition_text, child_instruction)
        self.variable_instruction = generic_instruction(variable_text)

    def convert_to_image(self, x: int, y: int, width: int) -> int:
        block_height = super().get_block_height()

        y = self.variable_instruction.convert_to_image(x, y, width)

        children_x, children_y, children_width = cti.draw_while_loop_front(self.instruction_text, x, y, width, block_height)
        self.draw_children(children_x, children_y, children_width)

        return y + block_height

    def get_block_width(self):
        return max(super().get_block_width(), self.variable_instruction.get_block_width())

    def get_block_height(self):
        return super().get_block_height() + self.variable_instruction.get_block_height()

    def __str__(self) -> str:
        res = str(self.variable_instruction) + '\n'
        res += "for\n"

        for instruction in self.children:
            res += "\t" + str(instruction) + '\n'
        
        return res