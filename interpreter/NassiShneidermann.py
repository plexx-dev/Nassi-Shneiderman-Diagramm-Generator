from typing import List
import logging

from draw.Iinstruction import Iinstruction
from interpreter import interpret_source as itp
from draw.code_to_image_wrapper import NSD_writer
import draw.code_to_image as cti


class NassiShneidermanDiagram:

    def __init__(self, do_debug: bool):
        self.instructions: List[Iinstruction] = []
        self.init_logging(do_debug)

    def init_logging(self, debug: bool):
        logLevel = logging.INFO
        if debug:
            logLevel = logging.DEBUG
        
        logging.basicConfig(level=logLevel)

    def set_font(self, font_filepath: str):
        cti.set_font(font_filepath)

    def _get_image_height(self) -> int:
        h = 0
        for inst in self.instructions:
            h += inst.getblksize()
        return int(h)

    def convert_to_image(self, filepath: str, x_size: int=200):
        image_y_sz = self._get_image_height()
        logging.info(f"Saving NSD to {filepath}.png...")
        with NSD_writer(filepath, x_size, image_y_sz):
            x, y = 0, 0

            for instruction in self.instructions:
                x, y = instruction.to_image(x, y, x_size)
            logging.info("Done!")

    def load_from_file(self, filepath:str):
        self.instructions = itp.load_instructions(filepath)