from NassiShneidermann import NassiShneidermanDiagram
from Iinstruction import *


def nassi(filepath:str ):
    NSD = NassiShneidermanDiagram(False)
    NSD.load_from_file(filepath)
    NSD.convert_to_image(filepath + "Nassi-Shneider-Diagramm", 500)