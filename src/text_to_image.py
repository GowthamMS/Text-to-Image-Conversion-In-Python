#!Python2.7
"""
Text to Image conversion using Pillow module in python
Copyrights (c) Text-to-Image-Conversion-In-Python 2018
Author: gowtham10ms@gmail.com
"""
from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont

__author__ = "Gowtham MS"
__copyright__ = "Copyright 2018, Text-to-Image-Conversion-In-Python"
__license__ = "GPL"
__version__ = "1.0"
__maintainer__ = "Gowtham MS"
__email__ = "gowtham10ms@gmail.com"
__status__ = "Production"

# pylint: disable=

IMAGE_NAME = 'image.png'
IMAGE_SIZE = ''
IMAGE_COLOR = (255, 255, 255)
IMAGE_TEXT = 'win-s1'
IMAGE_TEXT_POSITION = ''
IMAGE_TEXT_COLOR = (0, 0, 0)
IMAGE_TEXT_FONT_STYLE_TTF_FILE_PATH = 'Arial Narrow.ttf'
IMAGE_TEXT_FONT_SIZE = 11


if __name__ == '__main__':
    FONT = ImageFont.truetype(IMAGE_TEXT_FONT_STYLE_TTF_FILE_PATH, IMAGE_TEXT_FONT_SIZE)
    TESTIMG = Image.new('RGB', (1, 1))
    TESTDRAW = ImageDraw.Draw(TESTIMG)
    WIDTH, HEIGHT = TESTDRAW.textsize(IMAGE_TEXT, FONT)

    if IMAGE_SIZE:
        IMG = Image.new('RGBA', IMAGE_SIZE, IMAGE_COLOR)
    else:
        IMG = Image.new('RGBA', (WIDTH + 4, HEIGHT + 4), IMAGE_COLOR)
    DRAW = ImageDraw.Draw(IMG)

    if IMAGE_TEXT_POSITION:
        DRAW.text(IMAGE_TEXT_POSITION, IMAGE_TEXT, fill=IMAGE_TEXT_COLOR, FONT=FONT)
    else:
        DRAW.text((2, HEIGHT / 8), IMAGE_TEXT, fill=IMAGE_TEXT_COLOR, FONT=FONT)

    IMG.save(IMAGE_NAME)
