from random import randint

from PIL import Image

from .color_utils import change_color, hue_gen, rand_color
from .load import load_parts
from .models.layer import Layer


class Combinator:

    def __init__(self, layer_folder_path: str, width: int, height: int) -> None:
        self.parts = load_parts(layer_folder_path)
        self.size = (width, height)

    def combine_layers(self, layers: list[Layer], hue_up: bool = False) -> Image.Image:
        temp_img = Image.new('RGBA', self.size)

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

    def combine(self, hue_up_components: list[str] = []) -> Image.Image:
        img = Image.new('RGBA', self.size)

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
