from pytest import raises
import pytest
from source.validations import validate_color_RGB, validate_path, validate_size
from source.exceptions import EmptyPathError, EmptySizesError, ImposibleSizeError, PathNotFoundError, WrongTypeError


non_existing_path = './baldie/not_existing/'
main_path = './baldie/layers'
valid_size = (16, 16)
invalid_sizes = [(0, 0), (-16, -16), (-16, 16), (16, -16)]

# def test_get_files_name_path() -> None:
#     names_paths = get_files_name_path('')
#     assert names_paths == []


def test_validate_path_empty() -> None:
    with raises(EmptyPathError):
        assert validate_path()


def test_validate_path_non_found() -> None:
    with raises(PathNotFoundError):
        assert validate_path(non_existing_path)
        assert validate_path(main_path)


def test_validate_size_empty() -> None:
    with raises(EmptySizesError):
        assert validate_size(width=valid_size[0])
        assert validate_size(height=valid_size[0])
        assert validate_size()


def test_validate_size_invalid_sizes() -> None:
    with raises(ImposibleSizeError):
        for w, h in invalid_sizes:
            assert validate_size(w, h)


def test_validate_color_RGB() -> None:
    with raises(WrongTypeError):
        assert validate_color_RGB()
        assert validate_color_RGB((1, 2, 3))
