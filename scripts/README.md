All scripts assume python3.6+.

## Cowboyfy.py

Emojis in this library are made one of two ways. A subset are crafted carefully and meticulously by hand, with each pixel considered and loved. For the rest? We generate them programmatically. This is done using [cairosvg](https://cairosvg.org/).

### Command Line Arguments:
- *cowboy_input_dir* Location where the cowboy input dir is.
- *pensive_input_dir* Location where the pensive cowboy input dir is.
- *output_dir* Top level output dir
- *png_size* Side of a png square for the output

## tile_images.py

This is a drop dead-as-a-cow simple interface for taking a directory of images and combining each image side-by-side and row-by-row into a single image.

### Command Line Arguments:
- *input_dir* The directory that contains all the emojis to tile.
- *columns* The number of columns per row for your tiled image.
- *emoji_size* The width and height of the emoji in the tile in pixels. Emojis must be square and will be resized to this given size from their original size.
- *spacer* The amount of space between each emoji in pixels
