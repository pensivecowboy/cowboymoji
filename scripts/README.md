All scripts assume python3.6+.

## Cowboyfy.py

Emojis in this library are made one of two ways. A subset are crafted carefully and meticulously by hand, with each pixel considered and loved. For the rest? We generate them programmatically. This is done using [cairosvg](https://cairosvg.org/).

### Command Line Arguments:
- *cowboy_input_dir* Location where the cowboy input dir is.
- *pensive_input_dir* Location where the pensive cowboy input dir is.
- *output_dir* Top level output dir.
- *png_size* Side of a png square for the output.

## tile_images.py

This is a drop dead-as-a-cow simple interface for taking a directory of images and combining each image side-by-side and row-by-row into a single image.

### Command Line Arguments:
- *input_dir* The directory that contains all the emojis to tile.
- *output_name* the name of the output image.
- *columns* The number of columns per row for your tiled image.
- *emoji_size* The width and height of the emoji in the tile in pixels. Emojis must be square and will be resized to this given size from their original size.
- *spacer* The amount of space between each emoji in pixels.


### rename_cowboys.py
What if I don't want to use the emoji code as the emoji names, how do I convert to plain english? I wish I had an easy answer for you, partner. We've added the script we use over here 'round the ranch to convert the emoji names to names loosely based off of discord emoji names. However, there's rattlesnakes in the details. How you delimit spaces (icecream vs ice-cream vs ice_cream)? How do you denote skin shades for emojis that come in all skin colors? How do you tell apart a camel with one hump and a camel with two? Because there is no universal answer to problems like these, we can't promise this script meets your needs or will be maintained going forward.
