from .models.rgb import RGB
from random import randint

from PIL.Image import Image


def rand_color() -> RGB:
    r = randint(0, 255)
    g = randint(0, 255)
    b = randint(0, 255)
    return RGB(r, g, b)


def hue_gen(color: RGB, steps: int = 10) -> list[RGB]:
    if steps == 0:
        return [color]
    elif steps > 0:
        rs, gs, bs = color.r, color.g, color.b
        rf, gf, bf = 0, 0, 0
    else:
        rs, gs, bs = 0, 0, 0
        rf, gf, bf = color.r, color.g, color.b

    output = [RGB(rs, gs, bs)]

    k = -(steps/abs(steps))
    rdelta = int((k*rs-k*rf)/steps)
    gdelta = int((k*gs-k*gf)/steps)
    bdelta = int((k*bs-k*bf)/steps)

    for _ in range(abs(steps)-1):
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
