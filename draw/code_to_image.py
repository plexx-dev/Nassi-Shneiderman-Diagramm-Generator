"""code_to_image.py: #TODO"""

__author__      = "plexx, Weckyy702"

from typing import Tuple
from PIL import Image, ImageDraw, ImageFont
import os
import random

PADDING_X = 50
PADDING_Y = 5

BLOCK_OFFSET_RATIO = .1

datei_endung = ".png"

img = None
output_img = None

_bkp_font = ImageFont.truetype("res/fonts/NotoSans-Regular.ttf", 12) # ImageFont.load_default()

ERROR_TEXT = "Output image was not initialized! Make sure to call NSD_init first"

#in case set_font does funky stuff, backup the original font
font = _bkp_font


def NSD_init(x: float, y: float):
    #get input_img
    global img, output_img


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


def get_text_size(text: str) -> Tuple[int, int]:
    if not font:
        raise Exception(ERROR_TEXT)
    size = font.getsize(text)

    return (size[0]+PADDING_X, size[1]+PADDING_Y)



def draw_debug_tile(x:int, y:int, width:int, height:int) -> int:
    fill_color = (random.randint(0, 255),random.randint(0, 255), random.randint(0, 255))
    output_img.rectangle((x,y) + (x+width, y+height), outline=(0), fill=fill_color)

    return y + height

def draw_generic_instruction(instruction: str, x: int, y: int, width:int, height:int) -> int:
    if not output_img:
        raise Exception(ERROR_TEXT)

    #draw shit
    output_img.rectangle((x,y) + (x + width, y + height), outline=(0), width=1)

    #text shit
    output_img.multiline_text((x + width * .5, y + height * .5), instruction, font=font, anchor="mm", align="right", fill=(0))

    return y + height



def draw_if_statement(condition: str, x: int, y: int, true_width: int, block_width:int) -> Tuple[int, int, int, int]:
    """Draw an if statement into the NSD"""
    if not output_img:
        raise Exception(ERROR_TEXT)

    text_height = get_text_size(condition)[1]

    #condition
    output_img.rectangle((x, y) + (x + block_width, y + text_height), outline=(0), width=1) #Box around condition text
    output_img.multiline_text((x + true_width, y + text_height / 2), condition, fill=(0), font=font, anchor="mm", spacing=4, align='right')

    #fancy lines for the "true" and "false" labels
    output_img.line((x,y) + (x + true_width, y + text_height), fill=(0))
    output_img.line((x + block_width, y) + (x + true_width, y + text_height), fill=(0))
    # "true" and "false" labels
    output_img.text((x + 5, y + text_height), "true", font = font, fill = (0), anchor="ld")
    output_img.text((x + block_width - 5, y + text_height), "false", font = font, fill = (0), anchor="rd")

    #x and y of "true" and "false" label
    return x, y + text_height, x + true_width, y + text_height

def draw_while_loop_front(condition: str, x: int, y: int, block_width: int, block_height: int) -> Tuple[int, int, int]:

    if not output_img:
        raise Exception(ERROR_TEXT)

    text_height = get_text_size(condition)[1]

    block_offset = int(block_width * BLOCK_OFFSET_RATIO)

    #the box
    output_img.line((x,y) + (x + block_width, y), fill=(0))
    output_img.line((x,y) + (x, y + block_width), fill=(0))
    output_img.line((x + block_offset, y + text_height) + (x + block_width, y + text_height), fill=(0))
    output_img.line((x + block_width, y) + (x + block_width, y + text_height), fill=(0))
    output_img.line((x, y + block_height) + (x + block_offset, y + block_height ), fill=(0))
    output_img.line((x + block_offset, y + block_height) + (x + block_offset, y + text_height), fill=(0))

    #the text
    output_img.text((x + block_offset, y + text_height * .5), condition, font = font, fill = (0), anchor="lm")

    #the x, y offset then the children width
    return x + block_offset, y + text_height, block_width - block_offset

def draw_while_loop_back(condition: str, x: int, y: int, block_width: int, block_height: int):

    if not output_img:
        raise Exception(ERROR_TEXT)

    text_height = get_text_size(condition)[1]

    #the box
    output_img.line((x,y) + (x + block_width * .1, y), fill=0)
    output_img.line((x + block_width * .1, y) + (x + block_width * .1, y + block_height - text_height), fill=0)
    output_img.line((x + block_width * .1, y + block_height - text_height) + (x + block_width, y + block_height - text_height), fill=0)
    output_img.line((x + block_width, y + block_height - text_height) + (x + block_width, y + block_height), fill=0)
    output_img.line((x,y + block_height) + (x + block_width, y + block_height), fill=0)
    output_img.line((x,y) + (x, y + block_height), fill=0)

    #the text
    output_img.multiline_text((x + block_width * .1, y + block_height - text_height * .5), condition, font = font, fill = (0), anchor="lm")

    #the x, y offset then the x,y draw size (the canvas)
    return x + block_width * .1, y, block_width * .9

def NSD_save(filepath: str):
    """Save the created file"""
    filepath = filepath.removesuffix(datei_endung)
    img.save(filepath + datei_endung ,"PNG")