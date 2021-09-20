from source.models.part import Part
from source.models.attribute import Attribute
from PIL import Image
from source.models.layer import Layer
from pytest import raises
import pytest
from source.load import load_attributes, load_layers, load_parts, get_files_name_path
from source.exceptions import EmptyPathError, PathNotFoundError

images_path = './tests/testing_dir/images/part1/base'
attributes_path = './tests/testing_dir/images/part1/attributes'
part_path = './tests/testing_dir/images'

non_images_path = './tests/testing_dir/non_images'
not_existing_path = './baldie/layer'


def test_get_files_name_path_empty_path() -> None:
    assert get_files_name_path() == None
    assert get_files_name_path('') == None


def test_get_files_name_path_not_existing_path() -> None:
    assert get_files_name_path(not_existing_path) == None


def test_get_files_name_path_valid_path() -> None:
    expected = [('test_file1.txt', './tests/testing_dir/non_images\\test_file1.txt'),
                ('test_file2.txt', './tests/testing_dir/non_images\\test_file2.txt'),
                ('test_file3.txt', './tests/testing_dir/non_images\\test_file3.txt'), ]

    names_paths = get_files_name_path(non_images_path)

    for i in range(len(expected)):
        assert names_paths[i] == expected[i]


def test_load_layers_empty_path() -> None:
    assert load_layers() == None
    assert load_layers('') == None


def test_load_layers_not_existing_path() -> None:
    assert load_layers(not_existing_path) == None


def test_load_layers() -> None:
    names_paths = get_files_name_path(images_path)
    layers = load_layers(images_path)

    assert len(layers) == len(names_paths)

    for i in range(len(layers)):
        l = layers[i]
        assert type(l) == Layer
        assert l.id == names_paths[i][0]
        assert l.img == Image.open(names_paths[i][1])


def test_load_attributes_empty_path() -> None:
    assert load_attributes() == None
    assert load_attributes('') == None


def test_load_attributes_not_existing_path() -> None:
    assert load_attributes(not_existing_path) == None


def test_laod_attributes() -> None:
    names_paths = get_files_name_path(attributes_path)
    attributes = load_attributes(attributes_path)

    assert len(attributes) == len(names_paths)

    for i in range(len(attributes)):
        a = attributes[i]
        assert type(a) == Attribute
        assert a.name == names_paths[i][0]


def test_load_parts_empty_path() -> None:
    assert load_parts() == None
    assert load_parts('') == None


def test_load_parts_not_existing_path() -> None:
    assert load_parts(not_existing_path) == None


def test_load_parts() -> None:
    names_paths = get_files_name_path(part_path)
    parts = load_parts(part_path)

    assert len(parts) == len(names_paths)

    for i in range(len(parts)):
        p = parts[i]
        assert type(p) == Part
        assert p.name == names_paths[i][0]
