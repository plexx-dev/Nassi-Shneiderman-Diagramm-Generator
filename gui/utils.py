import logging
import os
from typing import Optional


from interpreter.NassiShneidermann import NassiShneidermanDiagram
from draw.Iinstruction import *


def nassi(filepath: str, output_path: str, outputname: str, gui, font_filepath: Optional[str]=None):
    NSD = NassiShneidermanDiagram(gui.debug_mode)
    if font_filepath != None:
        NSD.set_font(font_filepath)
    NSD.load_from_file(filepath)
    NSD.convert_to_image((output_path + '/' + outputname), 500)


def output(values):
    output_path = values['-OUTPUT FOLDER-']
    try:
        file_list = os.listdir(output_path)
    except:
        file_list = []
    fnames = [
        f
        for f in file_list
        if os.path.isfile(os.path.join(output_path, f))
        and f.lower().endswith(('.png', '.gif'))
    ]
    return fnames


def file_there(file):
    try:
        open((file + '.png'))
        return True
    except FileNotFoundError:
        return False
    except:
        raise
