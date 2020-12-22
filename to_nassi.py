from NassiShneidermann import NassiShneidermanDiagram
from Iinstruction import *


def nassi(filepath:str, output_path: str):
    NSD = NassiShneidermanDiagram(False)
    NSD.load_from_file(filepath)
    NSD.convert_to_image(output_path + "Nassi-Shneider-Diagramm", 500)

if __name__ == "__main__":
    nassi("input.java", "res/ouput/")