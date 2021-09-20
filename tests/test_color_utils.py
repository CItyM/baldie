from pytest import raises
from source.color_utils import *
from source.models.rgb import RGB
from PIL import Image


def test_rand_color():
    assert type(rand_color()) == RGB


def test_hue_gen_zero_steps():
    color = RGB(1, 2, 3)
    assert hue_gen(color, 0) == [color]


def test_hue_gen_negative_steps():
    color = RGB(1, 2, 3)
    steps = -10
    hues = hue_gen(color, steps)
    assert len(hues) == abs(steps)
    assert hues[0] == RGB(0, 0, 0)
    for h in hues:
        assert type(h) == RGB


def test_hue_gen_positive_steps():
    color = RGB(1, 2, 3)
    steps = 1000
    hues = hue_gen(color, steps)
    assert hues[0] == color
    assert len(hues) == steps
    for h in hues:
        assert type(h) == RGB


def test_change_color():
    imgs = [Image.new('RGBA', (16, 16)),
            Image.open('./tests/test_img.png')]
    rgb = RGB(1, 2, 3)
    for img in imgs:
        assert type(change_color(img, rgb)) == Image.Image
