import sys
from typing import Iterable
from PIL import Image, ImageDraw, ImageFont

output_dir = "res/output/"
datei_endung = ".png"

img = None
output_img = None
font = None


def NSD_init(x: float, y: float):
    #get input_img
    global img, output_img, font
    #img = Image.open(input_dir + file_name + datei_endung)
    img = Image.new("RGB", (x, y), "white")
    output_img = ImageDraw.Draw(img)
    #font = ImageFont.load_default()
    font = ImageFont.truetype("res/fonts/SpaceGrotesk-Light.ttf", 12)

def draw_generic_instruction(instruction: str, x, y, xsize, ysize) -> Iterable[float]:
    if not output_img:
        raise Exception("Output image was not initialized! Make sure to call NSD_init first")
    
    #size shit
    #text_y_size = font.getsize(instruction, direction="ltr")[1]
    #ysize = max(text_y_size, ysize) # ensure it is alway at least big enought to fit the text

    #draw shit
    output_img.rectangle((x,y) + (x + xsize, y + ysize), outline=(0), width=1)

    #text shit
    output_img.multiline_text((x + 5, y + ysize * .5), instruction, font=font, anchor="lm", align="right", fill=(0))

    return x, y + ysize




def draw_if_statement(condition: str, x: int, y: int, xsize: int, ysize: int):
    """Draw an if statement into the NSD"""
    if not output_img:
        raise Exception("Output image was not initialized! Make sure to call NSD_init first")

    output_img.line((x,y) + (x + xsize / 2, y + ysize / 4), fill=(0))
    output_img.line((x + xsize, y) + (x + xsize / 2, y + ysize / 4), fill=(0))
    output_img.rectangle((x, y + ysize / 4) + (x + xsize, y + ysize), outline=(0), width=1)
    output_img.rectangle((x, y) + (x + xsize, y + ysize / 4), outline=(0), width=1)
    output_img.line((x + xsize / 2, y + ysize / 4) + (x + xsize / 2, y + ysize), fill=(0))

    # condition text
    output_img.multiline_text((x + xsize / 2, y + ysize * .05 ), condition, fill=(0), font=font, anchor="mm", spacing=4, align='right')

    # true / false
    output_img.text((x + 5, y + ysize * .1875), "true", font = font, fill = (0), anchor="lm")
    output_img.text((x + xsize - 5, y + ysize * .1875), "false", font = font, fill = (0), anchor="rm")

    #first x,y,xsize,ysize of first box then of second first true and then false
    return x, y + ysize / 4, xsize / 2, ysize * .75, x + xsize / 2, y + ysize / 4, xsize / 2, ysize * .75

def draw_while_loop_front(condition: str, x: int, y: int, xsize: int, ysize: int):
    
    if not output_img:
        raise Exception("Output image was not initialized! Make sure to call NSD_init first")

    #ole #TODO

    #the box
    output_img.line((x,y) + (x + xsize, y), fill=(0))
    output_img.line((x,y) + (x, y + ysize), fill=(0))
    output_img.line((x + xsize * .1, y + ysize * .1) + (x + xsize, y + ysize * .1), fill=(0))
    output_img.line((x + xsize, y) + (x + xsize, y + ysize * .1), fill=(0))
    output_img.line((x, y + ysize) + (x + xsize * .1, y + ysize ), fill=(0))
    output_img.line((x + xsize * .1, y + ysize) + (x + xsize * .1, y + ysize * .1), fill=(0))

    #the text
    output_img.text((x + xsize * .1, y + ysize * .025), condition, font = font, fill = (0), anchor="lm")

    #the x, y offset then the x,y draw size (the canvas)
    return x + xsize * .1, y + ysize * .1, xsize * .9, ysize * .9

def draw_while_loop_back(condition: str, x: int, y: int, xsize: int, ysize: int):
    
    if not output_img:
        raise Exception("Output image was not initialized! Make sure to call NSD_init first")

    #ole #TODO

    #the box
    output_img.line((x,y) + (x + xsize * .1, y), fill=0)
    output_img.line((x + xsize * .1, y) + (x + xsize * .1, y + ysize * .9), fill=0)
    output_img.line((x + xsize * .1, y + ysize * .9) + (x + xsize, y + ysize * .9), fill=0)
    output_img.line((x + xsize, y + ysize * .9) + (x + xsize, y + ysize), fill=0)
    output_img.line((x,y + ysize) + (x + xsize, y + ysize), fill=0)
    output_img.line((x,y) + (x, y + ysize), fill=0)

    #the text
    output_img.text((x + xsize * .1, y + ysize * .95), condition, font = font, fill = (0), anchor="lm")

    #the x, y offset then the x,y draw size (the canvas)
    return x + xsize * .1, y, xsize * .9, ysize * .9

def NSD_save(filename: str):
    """Save the created file"""
    img.save(output_dir + filename + datei_endung , "PNG")

#x_offset , y_offset, x_size, y_size = draw_while_loop("lol", 0, 0, 100, 200)
if __name__ == "__main__":
    """Debugging :^)"""
    NSD_init(300, 500)
    #draw_if_statement("wenn das dann mach das", 0, 0, 100, 200)
    #print(x,y,xsize,ysize)
    #draw_generic_instruction(r"""Wolfgang.fuck("Nina")""", x, y, xsize, ysize)
    NSD_save("testink")