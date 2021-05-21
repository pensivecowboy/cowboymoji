#!/usr/bin/env python3


from cowboy_tool import CowboyTool
import argparse
import time
import os

def cli_to_args():
    """
    converts the command line interface to a series of args
    """
    cli = argparse.ArgumentParser(description="")
    cli.add_argument('-input_dir',
                     type=str, required=True,
                     help='Location where the input dir is.')
    cli.add_argument('-output_dir',
                     type=str, required=True,
                     help='Top level output dir')
    cli.add_argument('-png_size',
                     type=int, default=200,
                     help='Side of a png square for the output')
    return cli.parse_args()


def make_boring_emojis_into_cowboys(input_dir, output_dir, png_size, make_them_pensive_too=False):
    cowboy_tool = CowboyTool()
    # set up some defaults, and override some of them if we're making a pensive set.
    output_name = "cowboy"
    preview_image_name = "cowboy_full_set"
    preview_columns = 10
    if make_them_pensive_too:
       output_name = "pensive_cowboy"
       preview_image_name = "pensive_cowboy_full_set"
       preview_columns = 8

    output_path = f"{output_dir}/{output_name}"
    file_sizes = os.listdir(input_dir)
    for file_size in file_sizes:
       if file_size != ".DS_Store":
           files_to_convert = os.listdir(f"{input_dir}/{file_size}")
           for file in files_to_convert:
              # catch an edge case on macOS
              if file != ".DS_Store":
                  input_file = f"{input_dir}/{file_size}/{file}"
                  if make_them_pensive_too:
                      cowboy_tool.create_pensive_cowboy_emoji(input_file,
                                                              f"{output_path}/svg",
                                                              int(file_size))
                  else:
                      cowboy_tool.create_cowboy_emoji(input_file,
                                                      f"{output_path}/svg",
                                                      int(file_size))
    # copy files that were built in illustrator into the output directory
    cowboy_tool.copy_from_prebuilt_to_output(f"./prebuilt/{output_name}/svg",
                                             f"{output_path}/svg")
    # convert all the SVGs to pngs!
    cowboy_tool.convert_svg_to_png(f"{output_path}/svg",  f"{output_path}/png", png_size)
    # create a preview image
    preview_emoji_size = 100
    preview_emoji_spacer = 10
    cowboy_tool.tile_images(f"{output_path}/png",
                            f"../examples",
                            preview_image_name,
                            preview_columns,
                            preview_emoji_size,
                            preview_emoji_spacer)


def main():
   args = cli_to_args()
   overall_run_time = time.time()

   # make mood agnostic cowboys.
   print("Starting a cowboy generation task. Yee Haw!")
   make_boring_emojis_into_cowboys(f"{args.input_dir}/cowboy",
                                   args.output_dir,
                                   args.png_size,
                                   make_them_pensive_too=False)

   # make some cowboys and then telling them some bad news.
   print("Starting a cowboy generation task with a mood modifier! Haw Yee?")
   make_boring_emojis_into_cowboys(f"{args.input_dir}/pensive_cowboy",
                                   args.output_dir,
                                   args.png_size,
                                   make_them_pensive_too=True)
   print(f"Runtime:{time.time() - overall_run_time}s. Did you beat your high score?")


if __name__ == "__main__":
    main()
