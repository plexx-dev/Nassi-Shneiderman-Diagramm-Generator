import os


from interpreter.NassiShneidermann import NassiShneidermanDiagram
from draw.Iinstruction import *

def nassi(filepath:str, output_path: str, gui, font_filepath: str=None):
    NSD = NassiShneidermanDiagram(gui.debug_mode)
    if font_filepath:
        NSD.set_font(font_filepath)
    NSD.load_from_file(filepath)
    NSD.convert_to_image(output_path + "/Nassi-Shneider-Diagramm", 500)

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
