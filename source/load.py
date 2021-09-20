from glob import glob, iglob
from os import path

import PIL

from .models.attribute import Attribute
from .models.layer import Layer
from .models.part import Part
from .validations import validate_path


def get_files_name_path(pth: str = None) -> list[(str, str)]:
    try:
        validate_path(pth)
    except:
        return None

    pth = path.join(pth, '*')
    names = list(map(path.basename, iglob(pth)))
    paths = glob(pth)
    return list(zip(names, paths))


def load_layers(pth: str = None) -> list[Layer]:
    try:
        validate_path(pth)
    except:
        return None

    names_paths = get_files_name_path(pth)

    layers = [Layer(n, PIL.Image.open(p)) for n, p in names_paths]

    return layers


def load_attributes(pth: str = None) -> list[Attribute]:
    try:
        validate_path(pth)
    except:
        return None

    names_paths = get_files_name_path(pth)

    attributes = list[Attribute]()
    for n, p in names_paths:
        layers = load_layers(p)
        attributes.append(Attribute(n, layers))

    return attributes


def load_parts(pth: str = None) -> list[Part]:
    try:
        validate_path(pth)
    except:
        return None

    names_paths = get_files_name_path(pth)

    parts = list[Part]()
    for n, p in names_paths:
        base_layers = load_layers(path.join(p, 'base'))
        attributes = load_attributes(path.join(p, 'attribute'))

        parts.append(Part(n, base_layers, attributes))

    return parts
