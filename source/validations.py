from os import path

from .exceptions import (EmptyPathError, EmptySizesError, ImposibleSizeError,
                         PathNotFoundError, WrongTypeError)
from .models.rgb import RGB


def validate_path(pth: str = None) -> None:
    if not pth or len(pth) == 0:
        raise EmptyPathError

    if not path.exists(pth):
        raise PathNotFoundError(pth)


def validate_size(width: int = None, height: int = None) -> None:
    if width == None or height == None:
        raise EmptySizesError(width, height)

    if width <= 0 or height <= 0:
        raise ImposibleSizeError(width, height)


def validate_color_RGB(color: RGB = None) -> None:
    if type(color) != RGB:
        raise WrongTypeError(type(color), RGB)
