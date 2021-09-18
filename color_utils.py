from random import randint
from rgb import RGB

from PIL import Image, ImageColor

from color_utils import *


def rand_color() -> RGB:
    r = randint(0, 255)
    g = randint(0, 255)
    b = randint(0, 255)
    return RGB(r, g, b)


def hue_gen(color: RGB, steps: int = 10) -> list[RGB]:
    rs, gs, bs = color.r, color.g, color.b
    rf, gf, bf = ImageColor.getrgb('black')

    rdelta = int((rf-rs)/steps)
    gdelta = int((gf-gs)/steps)
    bdelta = int((bf-bs)/steps)

    output = [color]

    for _ in range(steps-1):
        rs += rdelta
        gs += gdelta
        bs += bdelta
        output.append(RGB(rs, gs, bs))

    return output


def change_color(img: Image, color: RGB) -> Image:
    temp_img = img.copy()

    r, g, b = color.r, color.g, color.b

    for x in range(img.width):
        for y in range(img.height):
            pxl = img.getpixel((x, y))
            if pxl != (0, 0, 0, 0):
                temp_img.putpixel((x, y), (r, g, b, 255))
    return temp_img
