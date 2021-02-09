#!/usr/bin/env python

"""utils.py: utils for gui.py"""

__author__      = "oleting, Weckyy702"


from errors.custom import NoPathError
from interpreter.NassiShneidermann import NassiShneidermanDiagram, Overwrite_behaviour, OB

from PySimpleGUI import one_line_progress_meter
from typing import Optional
import os
import logging

#types=types, remove_tages=modifier, comments=comments
def nassi(input_path: str, output_path: str, outputname: str, types, remove_tags, comments, gui, behaviour: Overwrite_behaviour, font_filepath: Optional[str]=None):
    NSD = NassiShneidermanDiagram(gui.debug_mode)
    output_directory = check_and_create_output_directory(output_path + '/' + outputname)
    
    if font_filepath != None:
        NSD.set_font(font_filepath)

    custom_tags = {"comments" : comments, "ignore" : remove_tags, "types" : types}
    
    is_empty = NSD.load_from_file(input_path, custom_tags)

    for scopes_index in NSD.convert_to_image(output_directory, on_conflict=behaviour):
        cancel = one_line_progress_meter('Progress', scopes_index, len(NSD.function_scopes), '-PROGRESSBAR-')
        
        if not cancel:
            break    
    
    return output_directory, is_empty

def check_and_create_output_directory(output_directory):
    try:
        if not os.path.exists(output_directory):
            os.makedirs(output_directory)
    except Exception as e:
        logging.error(e+ ': ' +  output_directory)
        raise
       
    return output_directory



def output(output_path, output_name=None):
    
    if output_path == '':
        raise NoPathError
    if output_name:
        output_path = output_path + '/' + output_name
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