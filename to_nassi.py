from NassiShneidermann import NassiShneidermanDiagram, nassi
from Iinstruction import *


def nassi(filepath):
    NSD = NassiShneidermanDiagram(True)
    NSD.load_from_file(filepath)
    NSD.convert_to_image("Nina", 500)