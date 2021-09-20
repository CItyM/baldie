from gen import set_up_combinator, img_gen_save
from pytest import raises
from source.exceptions import EmptyPathError
from source.exceptions import EmptySizesError
from source.exceptions import PathNotFoundError
from PIL.Image import Image
from source.combinator import Combinator

width, height = 16, 16
valid_path = './baldie/layers'
wrong_path = './baldie/layer'
test_img_path = './tests/test_img.png'


def test_set_up_combinator_empty_path() -> None:
    with raises(EmptyPathError):
        assert set_up_combinator('', width, height)
        assert set_up_combinator(width=width, height=height)


def test_set_up_combinator_empty_sizes() -> None:
    with raises(EmptySizesError):
        assert set_up_combinator(valid_path, width=width)
        assert set_up_combinator(valid_path, height=height)
        assert set_up_combinator(valid_path)


def test_set_up_combinator_non_existing_path() -> None:
    with raises(PathNotFoundError):
        assert set_up_combinator(wrong_path, width, height)


def test_set_up_combinator_viable_path() -> None:
    assert type(set_up_combinator(valid_path, width, height)) == Combinator


def test_img_gen_save_empty_path() -> None:
    with raises(EmptyPathError):
        assert img_gen_save('')
        assert img_gen_save()


def test_img_gen_save_viable_path() -> None:
    assert type(img_gen_save(test_img_path)) == Image


def test_img_gen_save_negative_pixels() -> None:
    with raises(ValueError):
        img_gen_save(test_img_path, -16)


def test_img_gen_save_zero_pixels() -> None:
    with raises(ValueError):
        img_gen_save(test_img_path, 0)
