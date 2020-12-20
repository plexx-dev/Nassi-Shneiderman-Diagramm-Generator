from code_to_image import NSD_save
from Iinstruction import Iinstruction
import logging
import re

class NassiShneidermanDiagram:

    def __init__(self, debug: bool=False) -> None:
        self.instructions: dict[str, Iinstruction] = {}
        self.init_logging(debug)

    def init_logging(self, debug: bool):
        logLevel = logging.INFO
        if debug:
            logLevel = logging.DEBUG
        
        logging.basicConfig(level=logLevel)
    
    def add_instruction(self, instruction: Iinstruction):
        instruction_key = "instruction#" + str(len(self.instructions))
        self.instructions[instruction_key] = instruction
        logging.debug("added instruction %s : %s", instruction_key, instruction.instruction_text)

    def convert_to_image(self, filename: str, x_size=200):
        logging.info(f"Saving NSD to {filename}.png")
        cti.NSD_init(x_size, 1000)
        x, y, x_sz = 0, 0, x_size
        for _k, instruction in self.instructions.items():
            x, y = instruction.to_image(x, y, x_sz, 200)
        cti.NSD_save(filename)

    @staticmethod
    def load_code_lines(filepath):
        lines = []
        try:
            with open(filepath) as file:
                for _line in file:
                    line:str = _line.strip()
                    if line and not re.match(r"""^//|^#|^COMMENT|^--""", line):
                        lines.append(line)
        except:
            logging.error(f"Failed to open input path {filepath}!")
        
        return lines

    def load_from_file(self, filepath: str):
        filtered_lines = self.load_code_lines(filepath)
        print(filtered_lines)
        num_brace
        for line in filtered_lines:
            if line.startswith("while("):

    
if __name__ == "__main__":
    """for debugging"""

    from Iinstruction import *

    NSD = NassiShneidermanDiagram(True)

    NSD.load_from_file("res/input/input.java")

    NSD.convert_to_image("Nina", 500)
