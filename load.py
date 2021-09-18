from glob import iglob
from os import path

from PIL import Image

from attribute import Attribute
from color_utils import *
from layer import Layer
from part import Part

PARTS_PATH = './baldie/layers/'


def load_layers(pth: str) -> list[Layer]:
    layers_pth = path.join(pth, '*')
    layers_name = list(map(path.basename, iglob(layers_pth)))

    layers = list[Layer]()

    for l in layers_name:
        layer_pth = path.join(pth, l)
        layers.append(Layer(l, Image.open(layer_pth)))

    return layers


def load_attributes(pth: str) -> list[Attribute]:
    if path.exists(pth) == False:
        return None

    attributes_pth = path.join(pth, '*')
    attributes_name = list(map(path.basename, iglob(attributes_pth)))

    attributes = list[Attribute]()
    for a in attributes_name:
        attribute_pth = path.join(pth, a)
        layers = load_layers(attribute_pth)
        attributes.append(Attribute(a, layers))

    return attributes


def load_parts() -> list[Part]:
    parts_pth = path.join(PARTS_PATH, '*')
    parts_name = list(map(path.basename, iglob(parts_pth)))

    parts = list[Part]()

    for p in parts_name:
        part_pth = path.join(PARTS_PATH, p)

        base_layers = load_layers(path.join(part_pth, 'base'))
        attributes = load_attributes(path.join(part_pth, 'attribute'))

        parts.append(Part(p, base_layers, attributes))

    return parts
