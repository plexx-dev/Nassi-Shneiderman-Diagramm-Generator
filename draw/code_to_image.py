from typing import Iterable
from PIL import Image, ImageDraw, ImageFont
import os

datei_endung = ".png"

img = None
output_img = None
_bkp_font = ImageFont.truetype("res/fonts/NotoSans-Regular.ttf", 12) #in case set_font does funky stuff, backup the original font
font = _bkp_font


def NSD_init(x: float, y: float):
    #get input_img
    global img, output_img
    #img = Image.open(input_dir + file_name + datei_endung)
    img = Image.new("RGB", (x, y), "white")
    output_img = ImageDraw.Draw(img)

def set_font(font_filepath: str):
    if not os.path.exists(font_filepath):
        raise FileNotFoundError("TTF file was not found!")
    global font
    try:
        font = ImageFont.truetype(font_filepath, 12)
    except:
        font = _bkp_font
        raise


def get_text_size(text: str):
    if not font:
        raise Exception("Output image was not initialized! Make sure to call NSD_init first")
    return font.getsize(text)

def draw_debug_tile(x, y, x_sz, y_sz):
    from random import randint

    output_img.rectangle((x, y) + (x + x_sz, y + y_sz), fill=(randint(0, 255)))
    return x, y + y_sz

def draw_generic_instruction(instruction: str, x, y, xsize, ysize) -> Iterable[float]:
    if not output_img:
        raise Exception("Output image was not initialized! Make sure to call NSD_init first")

    #draw shit
    output_img.rectangle((x,y) + (x + xsize, y + ysize), outline=(0), width=1)

    #text shit
    output_img.multiline_text((x + xsize * .5, y + ysize * .5), instruction, font=font, anchor="mm", align="right", fill=(0))

    return x, y + ysize

def draw_if_statement(condition: str, x: int, y: int, xsize: int, ysize: int):
    """Draw an if statement into the NSD"""
    if not output_img:
        raise Exception("Output image was not initialized! Make sure to call NSD_init first")

    text_y_size = font.getsize(condition)[1]

    output_img.line((x,y) + (x + xsize / 2, y + text_y_size), fill=(0))
    output_img.line((x + xsize, y) + (x + xsize / 2, y + text_y_size), fill=(0))
    output_img.rectangle((x, y + text_y_size) + (x + xsize, y + ysize), outline=(0), width=1)
    output_img.rectangle((x, y) + (x + xsize, y + text_y_size), outline=(0), width=1)
    output_img.line((x + xsize / 2, y + text_y_size) + (x + xsize / 2, y + ysize), fill=(0))

    # condition text
    output_img.multiline_text((x + xsize / 2, y + text_y_size / 2), condition, fill=(0), font=font, anchor="mm", spacing=4, align='right')

    # true / false
    output_img.text((x + 5, y + text_y_size), "true", font = font, fill = (0), anchor="ld")
    output_img.text((x + xsize - 5, y + text_y_size), "false", font = font, fill = (0), anchor="rd")

    #first x,y,xsize,ysize of first box then of second first true and then false
    return x, y + text_y_size, xsize / 2, ysize - text_y_size, x + xsize / 2, y + text_y_size, xsize / 2, ysize - text_y_size

def draw_while_loop_front(condition: str, x: int, y: int, xsize: int, ysize: int):
    
    if not output_img:
        raise Exception("Output image was not initialized! Make sure to call NSD_init first")

    text_y_sz = font.getsize(condition)[1]

    #the box
    output_img.line((x,y) + (x + xsize, y), fill=(0))
    output_img.line((x,y) + (x, y + ysize), fill=(0))
    output_img.line((x + xsize * .1, y + text_y_sz) + (x + xsize, y + text_y_sz), fill=(0))
    output_img.line((x + xsize, y) + (x + xsize, y + text_y_sz), fill=(0))
    output_img.line((x, y + ysize) + (x + xsize * .1, y + ysize ), fill=(0))
    output_img.line((x + xsize * .1, y + ysize) + (x + xsize * .1, y + text_y_sz), fill=(0))

    #the text
    output_img.text((x + xsize * .1, y + text_y_sz * .5), condition, font = font, fill = (0), anchor="lm")

    #the x, y offset then the x,y draw size (the canvas)
    return x + xsize * .1, y + text_y_sz, xsize * .9

def draw_while_loop_back(condition: str, x: int, y: int, xsize: int, ysize: int):
    
    if not output_img:
        raise Exception("Output image was not initialized! Make sure to call NSD_init first")

    text_y_sz = get_text_size(condition)[1]

    #the box
    output_img.line((x,y) + (x + xsize * .1, y), fill=0)
    output_img.line((x + xsize * .1, y) + (x + xsize * .1, y + ysize - text_y_sz), fill=0)
    output_img.line((x + xsize * .1, y + ysize - text_y_sz) + (x + xsize, y + ysize - text_y_sz), fill=0)
    output_img.line((x + xsize, y + ysize - text_y_sz) + (x + xsize, y + ysize), fill=0)
    output_img.line((x,y + ysize) + (x + xsize, y + ysize), fill=0)
    output_img.line((x,y) + (x, y + ysize), fill=0)

    #the text
    output_img.text((x + xsize * .1, y + ysize - text_y_sz * .5), condition, font = font, fill = (0), anchor="lm")

    #the x, y offset then the x,y draw size (the canvas)
    return x + xsize * .1, y, xsize * .9

def NSD_save(filepath: str):
    """Save the created file"""
    img.save(filepath + datei_endung ,"PNG")