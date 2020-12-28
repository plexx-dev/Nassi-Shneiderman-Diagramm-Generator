from typing import List
import logging
from enum import IntEnum
import os.path
import secrets

from draw.Iinstruction import Iinstruction
from interpreter import interpret_source as itp
from draw.code_to_image_wrapper import NSD_writer
import draw.code_to_image as cti

class Overwrite_behaviour(IntEnum):
    SKIP = 0
    OVERWWRITE = 1
    RANDOM_NAME = 2

OB = Overwrite_behaviour

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

    def check_conflicts(self, filepath:str, behavoiur: Overwrite_behaviour):
        if os.path.exists(filepath+".png"):
            if behavoiur == OB.SKIP:
                return None
            elif behavoiur == OB.OVERWWRITE:
                return filepath
            else:
                while os.path.exists(filepath+".png"):
                    filepath = filepath + str(secrets.token_hex(1))
                return filepath
        return filepath

    def convert_to_image(self, output_path: str, filename: str, on_conflict: Overwrite_behaviour=OB.SKIP, x_size: int=200):
        for i in range(len(self.scopes)):
            filepath = f"{output_path}/{filename}#{i}"
            filepath = self.check_conflicts(filepath, on_conflict)
            if filepath is not None:
                logging.info(f"Saving NSD to {filepath}...")
                print(f"Saving... to {filepath}")

                image_y_sz = self._get_image_height(i)
                with NSD_writer(filepath, x_size, image_y_sz):
                    scope = self.scopes[i]
                    x, y = 0, 0
                    for instruction in scope:
                        x, y = instruction.to_image(x, y, x_size)
                    logging.info("Done!")

    def load_from_file(self, filepath:str):
        self.scopes = itp.load_instructions(filepath)