import os
from typing import Optional

from errors.custom import NoPathError
from interpreter.NassiShneidermann import NassiShneidermanDiagram, Overwrite_behaviour, OB
from draw.Iinstruction import *

def nassi(input_path: str, output_path: str, outputname: str, gui, behaviour: Overwrite_behaviour, font_filepath: Optional[str]=None):
    NSD = NassiShneidermanDiagram(gui.debug_mode)
    
    if font_filepath != None:
        NSD.set_font(font_filepath)
    
    NSD.load_from_file(input_path)
    NSD.convert_to_image(output_path, outputname, on_conflict=behaviour, x_size=750)


def output(values):
    output_path = values['-OUTPUT FOLDER-']
    if output_path == '':
        raise NoPathError
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