from typing import List
import logging

from draw.Iinstruction import Iinstruction
from interpreter import interpret_source as itp
from draw import code_to_image as cti


class NassiShneidermanDiagram:

    def __init__(self, do_debug: bool):
        self.instructions: List[Iinstruction] = []
        self.init_logging(do_debug)

    def init_logging(self, debug: bool):
        logLevel = logging.INFO
        if debug:
            logLevel = logging.DEBUG
        
        logging.basicConfig(level=logLevel)
    
    def add_instruction(self, instruction: Iinstruction):
        self.instructions.append(instruction)

    def get_image_height(self) -> int:
        h = 0
        for inst in self.instructions:
            h += inst.getblksize()
        return int(h)

    def convert_to_image(self, filename: str, x_size: int=200):
        logging.info(f"Saving NSD to {filename}.png")
        image_y_sz = self.get_image_height()
        cti.NSD_init(x_size, image_y_sz)
        x, y = 0, 0

        for instruction in self.instructions:
            x, y = instruction.to_image(x, y, x_size)
        
        cti.NSD_save(filename)

    def load_from_file(self, filepath:str):
        instructions = itp.load_instructions(filepath)
        self.add_instructions_from_scope(instructions)

    def add_instructions_from_scope(self, scope: List[Iinstruction]):
        for inst in scope:
            self.add_instruction(inst)


    
if __name__ == "__main__":
    NSD = NassiShneidermanDiagram(True)

    NSD.load_from_file("res/input/input.java")

    NSD.convert_to_image("Nina", 500)
