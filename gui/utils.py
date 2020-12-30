from errors.custom import NoPathError
from interpreter.NassiShneidermann import NassiShneidermanDiagram, Overwrite_behaviour, OB

from typing import Optional
import os
import logging


def nassi(input_path: str, output_path: str, outputname: str, gui, behaviour: Overwrite_behaviour, font_filepath: Optional[str]=None):
    NSD = NassiShneidermanDiagram(gui.debug_mode)
    directory = output_path + '/' + outputname
    
    if font_filepath != None:
        NSD.set_font(font_filepath)

    try:
        if not os.path.exists(directory):
            os.makedirs(directory)
    except OSError:
        logging.error('Error: Creating directory. ' +  directory)
    except:
        raise
    
    NSD.load_from_file(input_path)
    NSD.convert_to_image(directory, on_conflict=behaviour, x_size=750)

    return directory


def output(folder):
    if folder:
        output_path = folder
    else:
        raise

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