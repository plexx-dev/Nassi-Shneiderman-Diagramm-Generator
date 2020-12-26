from typing import List
import logging

from draw.Iinstruction import Iinstruction
from interpreter import interpret_source as itp
from draw import code_to_image as cti


class NassiShneidermanDiagram:

    def __init__(self, gui):
        self.instructions: dict[str, Iinstruction] = {}
        self.init_logging(gui.debug_mode)

    def init_logging(self, debug: bool):
        logLevel = logging.INFO
        if debug:
            logLevel = logging.DEBUG
        
        logging.basicConfig(level=logLevel)
    
    def add_instruction(self, instruction: Iinstruction):
        instruction_key = "instruction#" + str(len(self.instructions))
        self.instructions[instruction_key] = instruction
        logging.debug("added instruction %s : %s", instruction_key, instruction.instruction_text)

    def convert_to_image(self, filename: str, x_size: int=200):
        logging.info(f"Saving NSD to {filename}.png")
        cti.NSD_init(x_size, 5000)
        x, y, x_sz = 0, 0, x_size
        for _k, instruction in self.instructions.items():
            x, y = instruction.to_image(x, y, x_sz)
        cti.NSD_save(filename)

    def load_from_file(self, filepath:str):
        src_code = itp.load_src(filepath)
        global_scope = itp.get_instructions_in_scope(src_code)[0]
        self.add_instructions_from_scope(global_scope)

    def add_instructions_from_scope(self, scope: List[Iinstruction]):
        for inst in scope:
            self.add_instruction(inst)


    
if __name__ == "__main__":
    NSD = NassiShneidermanDiagram(True)

    NSD.load_from_file("res/input/input.java")

    NSD.convert_to_image("Nina", 500)
