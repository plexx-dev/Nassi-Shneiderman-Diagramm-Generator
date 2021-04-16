"""Iinstruction.py: Instruction classes to turn the lexing results into an image"""

__author__      = "Weckyy702"


from typing import Iterable, List, Tuple
from abc import ABCMeta, abstractmethod
from draw import code_to_image as cti

class Iinstruction(metaclass=ABCMeta):
    """Base class for all instructions"""

    def __init__(self, instruction_text: str) -> None:
        self.instruction_text = instruction_text

    @abstractmethod
    def to_image(self, x:int, y:int, x_sz: int) -> Tuple[float, float, float]:
        pass

    @abstractmethod
    def getblkheight(self) -> float:
        pass

    @abstractmethod
    def getblkwidth(self) -> float:
        pass

    @abstractmethod
    def __str__(self) -> str:
        pass

    def _getblkheight(self) -> float:
        return cti.get_text_size(self.instruction_text)[1] + cti.PADDING_Y #padding

    def _getblkwidth(self) -> float:
        return cti.get_text_size(self.instruction_text)[0] + cti.PADDING_X #padding


class generic_instruction(Iinstruction):
    """Any instruction that is not a control structure"""

    def __init__(self, instruction_text: str) -> None:
        super().__init__(instruction_text)
 
    def to_image(self, x:int, y:int, x_sz: int) -> Tuple[float, float, float]:
        return cti.draw_generic_instruction(self.instruction_text, x, y, x_sz, self.getblkheight())

    def getblkheight(self) -> float:
        return self._getblkheight()
    
    def getblkwidth(self) -> float:
        return self._getblkwidth()

    def __str__(self) -> str:
        return self.instruction_text

class if_instruction(Iinstruction):
    """Conditional structurewdas
        NOT.
        A.
        LOOP
    """

    def __init__(self, instruction_text: str, true_case: List[Iinstruction], false_case: List[Iinstruction]=None) -> None:
        super().__init__(instruction_text)
        self.true_case = true_case
        self.false_case = false_case

    def get_trueheight(self) -> float:
        sz = 0.0
        for inst in self.true_case:
            sz += inst.getblkheight()
        return sz

    def get_falseheight(self) -> float:
        sz = 0.0
        if self.false_case:
            for inst in self.false_case:
                sz += inst.getblkheight()
        return sz

    def get_truewidth(self) -> float:
        w = 200.0

        for inst in self.true_case:
            w = max(w, inst.getblkwidth())
        
        return w
    
    def get_falsewidth(self) -> float:
        w = 200.0

        if self.false_case:
            for inst in self.false_case:
                w = max(w, inst.getblkwidth())

        return w

    def getblkheight(self) -> float:
        return self._getblkheight() + max(self.get_trueheight(), self.get_falseheight())

    def getblkwidth(self) -> float:
        text_width, true_width, false_width = self.get_widths()

        return max(text_width, true_width+false_width)

    def get_widths(self) -> Tuple[float, float, float]:
        text_width = self._getblkwidth()
        true_width = self.get_truewidth()
        false_width = self.get_falsewidth()

        true_width = max(text_width/2, true_width)
        false_width = max(text_width/2, false_width)
        true_width = max(text_width-false_width, true_width)

        return text_width, true_width, false_width
        
    
    def to_image(self, x:int, y:int, x_sz: int) -> Tuple[float]:
        _, true_w, false_w = self.get_widths()
        true_x, true_y, true_w, false_x, false_y, false_w = cti.draw_if_statement(
            self.instruction_text, x, y, true_w, false_w, self.getblkheight()
        )
        self.draw_true_case(true_x, true_y, true_w)
        self.draw_false_case(false_x, false_y, false_w)
        blk_size = self.getblkheight()
        return x, y + blk_size

    def draw_true_case(self, x: float, y:float, x_sz:float):
        for instruction in self.true_case:
            x, y = instruction.to_image(x, y, x_sz)[0:2]

    def draw_false_case(self, x: float, y:float, x_sz:float):
        if self.false_case:
            for instruction in self.false_case:
                x, y = instruction.to_image(x, y, x_sz)[0:2]

    def __str__(self) -> str:
        res = f"if({self.instruction_text}) {'{'}\n"
        for inst in self.true_case:
            res += '\t'+str(inst)+";\n"
        res += "}"
        if self.false_case:
            res += " else {\n"
            for inst in self.true_case:
                res += '\t'+str(inst)+";\n"
            res += "}"
        return res

class while_instruction_front(Iinstruction):

    def __init__(self, condition: str, instructions: List[Iinstruction]) -> None:
        super().__init__(condition)
        self.child_instructions = instructions

    def get_children_height(self) -> float:
        children_sz = 0
        for inst in self.child_instructions:
            children_sz += inst.getblkheight()
        return children_sz

    def get_children_width(self) -> float:
        w = 0.0
        for inst in self.child_instructions:
            w = max(w, inst.getblkheight())
        return w

    def getblkheight(self) -> float:
        return self._getblkheight() + self.get_children_height()

    def getblkwidth(self) -> float:
        return max(self._getblkwidth(), self.get_children_width())
    
    def to_image(self, x:int, y:int, x_sz: int) -> Tuple[float]:
        children_x, children_y, children_sz_x = cti.draw_while_loop_front(self.instruction_text, x, y, x_sz, self.getblkheight())
        self.draw_children(children_x, children_y, children_sz_x)

        return x, y + self.getblkheight()


    def draw_children(self, x:float, y:float, x_sz:float):
        for inst in self.child_instructions:
            x, y = inst.to_image(x, y, x_sz)[0:2]
        return self.get_children_height()

    def __str__(self) -> str:
        res = "while(" + self.instruction_text + "){\n"
        for inst in self.child_instructions:
            res += '\t'+str(inst)+";\n"
        res += '}'
        return res


class while_instruction_back(while_instruction_front):
    def __init__(self, condition: str, instructions: List[Iinstruction]) -> None:
        super().__init__(condition, instructions)
    
    def to_image(self, x:int, y:int, x_sz: int):
        children_x, children_y, children_sz_x = cti.draw_while_loop_back(self.instruction_text, x, y, x_sz, self.getblkheight())
        self.draw_children(children_x, children_y, children_sz_x)
        return x, y + self.getblksize()

    def __str__(self) -> str:
        res = "do{\n"
        for inst in self.child_instructions:
            res += '\t' +str(inst) + ";\n"
        res += f"{'}'}while({self.instruction_text});"
        return res

class for_instruction(while_instruction_front):
    def __init__(self, variable_def: str, condition: str, instructions: List[Iinstruction]) -> None:
        super().__init__(condition, instructions)
        self.variable_instruction = generic_instruction(variable_def) if variable_def else None

    def to_image(self, x: int, y: int, x_sz: int) -> Tuple[float]:
        if self.variable_instruction:
            x, y, _ = self.variable_instruction.to_image(x, y, x_sz)
        return super().to_image(x, y, x_sz)

    def getblkheight(self) -> float:
        if self.variable_instruction:
            return super().getblkheight()+self.variable_instruction.getblkheight()
        return super().getblkheight()

    def getblkwidth(self) -> float:
        if self.variable_instruction:
            return max(super().getblkwidth(), self.variable_instruction.getblkwidth())
        return super().getblkwidth()

    def __str__(self) -> str:
        if self.variable_instruction:
            return self.variable_instruction.__str__()+';\n' + super().__str__()
        return super().__str__()