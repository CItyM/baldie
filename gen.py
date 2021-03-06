from source.validations import validate_path, validate_size
import argparse
from os import getenv

import matplotlib.pyplot as plt
from dotenv import load_dotenv
from PIL.Image import BOX, Image

from source.combinator import Combinator

load_dotenv()
LAYERS_FOLDER_PATH = getenv('LAYERS_FOLDER_PATH')
WIDTH = int(getenv('WIDTH'))
HEIGHT = int(getenv('HEIGHT'))
HUE_PARTS = getenv('HUE_PARTS').split(' ')


def set_up_cli() -> None:
    parser = argparse.ArgumentParser(
        description="Baldie: generative NFT like images")

    parser.add_argument("-s", "--show", action='store_true',
                        help="Show the image after generated.")

    parser.add_argument("-o", "--one", action='store', nargs=1, type=str, metavar='out-file',
                        help="Generates only one image.")

    parser.add_argument("-m", "--many", action='store', nargs='+', type=str, metavar='out-file',
                        help="Generates many images.(If given a single out-file (csv), read out-files from it.)")

    parser.add_argument("-sz", "--size", action='store', nargs=1, type=int, metavar='pxls', default=2160,
                        help="Size of an image's side in pixels.")
    return parser.parse_args()


def set_up_combinator(layers_folder_path: str = None, width: int = None, height: int = None) -> Combinator:
    validate_path(layers_folder_path)

    validate_size(width, height)

    combinator = Combinator(layers_folder_path, width, height)
    return combinator


combinator = set_up_combinator(LAYERS_FOLDER_PATH, WIDTH, HEIGHT)


def img_gen_save(out_file: str = None, pxls: int = 2160) -> Image:
    validate_path(out_file)

    img = combinator.combine(HUE_PARTS)
    img = img.resize((pxls, pxls), BOX)
    img.save(out_file)

    return img


def main() -> None:
    try:
        args = set_up_cli()

        if args.one:
            img = img_gen_save(args.one[0], args.size)
            if args.show:
                show(img)

        if len(args.many) == 1:
            with open(args.many[0], 'r') as f:
                out_files = f.readlines()
            out_files = ''.join(out_files)
            out_files = out_files.split(',')
            for of in out_files:
                img = img_gen_save(of, args.size)
                if args.show:
                    show(img)

        elif len(args.many) > 1:
            for of in args.many:
                img = img_gen_save(of, args.size)
                if args.show:
                    show(img)
    except Exception as e:
        print(e)
        exit(1)


def show(img: Image) -> None:
    plt.imshow(img)
    plt.show()


if __name__ == '__main__':
    main()
