#!/usr/bin/env python3

import argparse
import os
import sys
from PIL import Image

def cli_to_args():
    """
    converts the command line interface to a series of args
    """
    cli = argparse.ArgumentParser(description="")
    cli.add_argument('-input_dir',
                     type=str, required=True,
                     help='The directory that contains all the emojis to tile.')
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

   input_dir = args.input_dir
   image_list = os.listdir(args.input_dir)
   image_list = sorted(image_list)
   max_width = args.columns
   emoji_side = args.emoji_size
   emoji_spacer = args.spacer
   emoji_full_size = emoji_side + emoji_spacer

   image_width = emoji_full_size * max_width
   if len(image_list) < max_width:
       image_width = emoji_full_size * len(image_list)

   image_height = (int(len(image_list) / max_width)) * emoji_full_size
   if (len(image_list) % max_width) > 0:
      image_height = image_height + emoji_full_size

   output_image = Image.new('RGBA', (image_width, image_height), (0, 0, 0, 0))
   cur_x = 0
   cur_y = 0
   for image in image_list:
      emoji = Image.open(f"{input_dir}/{image}", 'r')
      emoji_resized = emoji.resize((emoji_side, emoji_side))
      output_image.paste(emoji_resized, (cur_x * emoji_full_size, cur_y * emoji_full_size))
      cur_x = cur_x + 1
      if cur_x == max_width:
         cur_x = 0
         cur_y = cur_y + 1
   output_image.save("output.png", format="png")

if __name__ == "__main__":
    main()
