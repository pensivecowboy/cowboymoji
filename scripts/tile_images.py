#!/usr/bin/env python3

import argparse
from cowboy_tool import CowboyTool

def cli_to_args():
    """
    converts the command line interface to a series of args
    """
    cli = argparse.ArgumentParser(description="")
    cli.add_argument('-input_dir',
                     type=str, required=True,
                     help='The directory that contains all the emojis to tile.')
    cli.add_argument('-output_name',
                     type=str, required=False, default="output",
                     help='The final name of the output image.')
    cli.add_argument('-columns',
                     type=int, required=False, default=10,
                     help='The number of columns per row for your tiled image.')
    cli.add_argument('-emoji_size',
                     type=int, required=False, default=100,
                     help='The width and height of the emoji in the tile in pixels. '
                          'Emojis must be square and will be resized to this given '
                          'size from their original size.')
    cli.add_argument('-spacer',
                     type=int, required=False, default=10,
                     help='The amount of space between each emoji in pixels')
    return cli.parse_args()


def main():
   args = cli_to_args()
   cowboy_tool = CowboyTool()
   cowboy_tool.tile_images(args.input_dir, args.output_name, args.columns, args.emoji_size, args.spacer)


if __name__ == "__main__":
    main()
