from random import randint

from PIL import Image

from color_utils import *
from layer import Layer
from load import load_parts


class Combinator:
    parts = load_parts()

    def combine_layers(self, layers: list[Layer], hue_up: bool = False) -> Image:
        temp_img = Image.new('RGBA', (16, 16))

        hues = hue_gen(rand_color(), len(layers)*2)

        for i in range(len(layers)):
            layer = layers[i]
            if hue_up:
                color = hues[i]
            else:
                color = rand_color()

            colored = change_color(layer.img, color)
            temp_img.paste(colored, mask=layer.img)

        return temp_img

    def combine(self, hue_up_components: list[str] = []) -> Image:
        img = Image.new('RGBA', (16, 16))

        for p in self.parts:
            temp = self.combine_layers(p.base, (p.name in hue_up_components))
            img.paste(temp, mask=temp)
            if p.attributes:
                l = len(p.attributes)
                i = randint(0, l)
                if i < l:
                    a = p.attributes[i]
                    temp = self.combine_layers(
                        a.layers, (a.name in hue_up_components))

                    img.paste(temp, mask=temp)

        return img
