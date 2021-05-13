#!/usr/bin/env python3

import svgutils.transform as sg
from svgutils.compose import Figure
from pathlib import Path
import cairosvg
import sys
import os
import unicodedata
from shutil import copytree

class CowboyTool:
   def __init__(self):
      # twemoji emojis are 36x36 by default
      self.standard_size = 36
      # load the glorious hat emoji
      self.all_powerful_hat = sg.fromfile('hat.svg')
      self.all_powerful_root = self.all_powerful_hat.getroot()


   def create_cowboy_emoji(self, input, output_dir, offset):
      """
      Takes an emoji as input and applies a cowboy hat. Yeah,
      I'm glad it exists too.
      """
      print(f"cowboyfy-ing {input}.... yee haw.")
      # create output path, if it doesn't exist
      Path(output_dir).mkdir(parents=True, exist_ok=True)
      # get filename without path or extension
      input_filename = Path(input).stem

      # load input svg
      input_file = sg.fromfile(input)
      # move input slightly down
      input_root = input_file.getroot()
      input_root.moveto(0, offset)

      # apply the offset to the expected height
      final_height = self.standard_size + offset

      # overlay the emojis on a workspace and save that as an output svg
      Figure(f"{self.standard_size}px",f"{final_height}px",
	     input_root,
	     self.all_powerful_root).save(f"{output_dir}/{input_filename}.svg")


   def create_pensive_cowboy_emoji(self, input, output_dir, offset):
      """
      Takes an emoji as input and applies a cowboy hat, then puts it in a city
      and tells its some bad news.
      """
      print(f"pensiving and cowboyfy-ing {input}.... haw yee.")
      # create output path, if it doesn't exist
      Path(output_dir).mkdir(parents=True, exist_ok=True)
      # get filename without path or extension
      input_filename = Path(input).stem

      # load input svg
      input_file = sg.fromfile(input)
      # move input slightly down
      input_root = input_file.getroot()
      input_root.moveto(0, offset)


      # load the all knowing pensive face svg.
      all_knowing_face = sg.fromfile('pensive.svg')
      # move pensive face to same spot as input svg
      all_knowing_root = all_knowing_face.getroot()
      # the pensive face is 20x26, so account for that and move it, move it.
      all_knowing_root.moveto(5, offset + 8)

      # apply the offset to the expected height
      final_height = self.standard_size + offset
      # overlay the emojis on a workspace and save that as an output svg
      Figure(f"{self.standard_size}px", f"{final_height}px",
             input_root,
             self.all_powerful_root,
             all_knowing_root).save(f"{output_dir}/{input_filename}.svg")


   def copy_from_prebuilt_to_output(self, prebuilt_dir, output_dir):
      prebuilt = Path(prebuilt_dir)
      output = Path(output_dir)
      if not prebuilt.exists():
         print("WHERE IS YOUR PREBUILT DIR!? Is it maybe on vacation?")
         exit()
      if not output.exists():
         print("WHERE IS YOUR OUTPUT DIR!? Is it maybe talking to its lawyer?")
         exit()
      copytree(prebuilt, output, dirs_exist_ok=True)


   def convert_svg_to_png(self, input_dir, output_dir, side):
      print(f"Making this dir {output_dir}")
      Path(output_dir).mkdir(parents=True, exist_ok=True)
      files_to_convert = os.listdir(input_dir)
      for file in files_to_convert:
         input_file = f"{input_dir}/{file}"
         input_filename = Path(input_file).stem
         output_file = f"{output_dir}/{input_filename}.png"
         print(f"Generating png: {output_file}")
         #cairosvg.svg2pdf(url=input_file, write_to=output_file) #TODO why does this just fail without error? Probably my environment... but then why does the command line work?
         os.system(f"cairosvg {input_file} -f png -o {output_file} --output-width {side} --output-height {side}")


#def convert_unicode_to_simple_name(input):
#   input_filename = Path(input).stem
#   input_strings = input_filename.split("-")
#   cldr = ""
#   print(len(input_strings))
#   for substring in input_strings:
#      #print(substring)
#      cldr = unicodedata.name(chr(int(substring, 16)))
#   print(cldr)
