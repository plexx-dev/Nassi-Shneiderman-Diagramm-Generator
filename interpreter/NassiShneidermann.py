from interpreter.interpret_source import Function_scope
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
        self.function_scopes: List[Function_scope] = []
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
        for inst in self.function_scopes[scope_index]:
            h += inst.getblksize()
        return int(h)

    def _save_scope(self, scope_index: int, output_path: str, x_size: int):
        """DEBUGING ONLY"""
        scope = self.function_scopes[scope_index]
        image_y_sz = self._get_image_height(scope_index)
        with NSD_writer(output_path, x_size, image_y_sz):
            x, y = 0, 0
            for instruction in scope.contents:
                x, y = instruction.to_image(x, y, x_size)

    def check_conflicts(self, filepath:str, behavoiur: Overwrite_behaviour):
        if os.path.exists(filepath + ".png"):
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
        for i in range(len(self.function_scopes)):
            filepath = f"{output_path}/{filename}#{i}"
            filepath = self.check_conflicts(filepath, on_conflict)
            if filepath is not None:
                logging.info(f"Saving NSD to {filepath}...")

                try:
                    self._save_scope(i, filepath, x_size)
                except Exception as e:
                    logging.error(f"Failed to save image {filepath} with error '{e}'")
                except:
                    logging.error(f"Failed to save image {filepath}. Unknown error")
                    raise

    def load_from_file(self, filepath:str):
        self.function_scopes = itp.load_scoped_instructions(filepath)