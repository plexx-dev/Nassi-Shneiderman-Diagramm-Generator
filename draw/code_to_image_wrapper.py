"""code_to_image_wrapper.py: #TODO"""

__author__      = "Weckyy702"


import draw.code_to_image as cti

class NSD_writer(object):
    def __init__(self, filepath: str, x_sz: int, y_sz: int) -> None:
        self.filepath = filepath
        self.x_sz = x_sz
        self.y_sz = y_sz
    
    def __enter__(self):
        cti.NSD_init(self.x_sz, self.y_sz)
    
    def __exit__(self, _, __, ___):
        cti.NSD_save(self.filepath)