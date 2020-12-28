from typing import List
import logging

from draw.Iinstruction import Iinstruction
from interpreter import interpret_source as itp
from draw.code_to_image_wrapper import NSD_writer
import draw.code_to_image as cti


class NassiShneidermanDiagram:

    def __init__(self, do_debug: bool):
        self.scopes: List[List[Iinstruction]] = []
        self.init_logging(do_debug)

    def init_logging(self, debug: bool):
        logLevel = logging.INFO
        if debug:
            logLevel = logging.DEBUG
        
        logging.basicConfig(level=logLevel)

    def set_font(self, font_filepath: str):
        cti.set_font(font_filepath)

    def _get_image_height(self, scope_index: int) -> int:
        h = 0
        for inst in self.scopes[scope_index]:
            h += inst.getblksize()
        return int(h)

    def _save_scope(self, scope_name: str, scope_instructions: List[Iinstruction]):
        """DEBUGING ONLY"""
        image_y_sz = 1000
        x, y, = 0, 0
        with NSD_writer(f"./{scope_name}", 1000, image_y_sz):
            x, y = 0, 0
            for instruction in scope_instructions:
                x, y = instruction.to_image(x, y, 1000)

    def convert_to_image(self, output_path: str, filename: str, x_size: int=200):
        for i in range(len(self.scopes)):
            filepath = f"{output_path}/{filename}#{i}"
            logging.info(f"Saving NSD to {filepath}.png...")

            image_y_sz = self._get_image_height(i)
            with NSD_writer(filepath, x_size, image_y_sz):
                scope = self.scopes[i]
                x, y = 0, 0
                for instruction in scope:
                    x, y = instruction.to_image(x, y, x_size)
                logging.info("Done!")

    def load_from_file(self, filepath:str):
        self.scopes = itp.load_instructions(filepath)