from NassiShneidermann import NassiShneidermanDiagram
from Iinstruction import *


def nassi(filepath):
    NSD = NassiShneidermanDiagram(False)
    NSD.load_from_file(filepath)
    NSD.convert_to_image("Nassi-Shneider-Diagramm", 500)