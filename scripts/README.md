All scripts assume `python3.6+`.

## Cowboyfy.py

Emojis in this library are made one of two ways. A subset are crafted carefully and meticulously by hand, with each pixel considered and loved. The rest we generate programmatically. This is done using [cairosvg](https://cairosvg.org/).

#### Command Line Arguments:
- *cowboy_input_dir* Location where the cowboy input dir is.
- *pensive_input_dir* Location where the pensive cowboy input dir is.
- *output_dir* Top level output dir.
- *png_size* Side of a png square for the output.

## tile_images.py

This is a drop dead-as-a-cow simple interface for taking a directory of images and combining each image side-by-side and row-by-row into a single image.

#### Command Line Arguments:
- *input_dir* The directory that contains all the emojis to tile.
- *output_name* the name of the output image.
- *columns* The number of columns per row for your tiled image.
- *emoji_size* The width and height of the emoji in the tile in pixels. Emojis must be square and will be resized to this given size from their original size.
- *spacer* The amount of space between each emoji in pixels.


## rename_cowboys.py

Sometimes, strangers walk up to our ranch and ask: "Hey partner, what if I don't want to use the emoji code as the emoji names, how do I convert to plain english?"

I wish I had an easy answer for you, partner. The root issue is that the "plain english" names for emojis aren't standardized across services. So, we've added the script we use 'round the ranch to convert the Unicode emoji codes to names that _mostly_ follow Discord's emoji names. However, there's rattlesnakes in the details and our solution may only get you part of the way there for integration into other services. For instance, for your use case, how should you handle spaces? (`ice_cream` vs `ice-cream` vs `icecream`). How should you handle emojis with gender/age/skin/clothing variants (`old_woman` vs `old_f`)? How do you tell apart a camel with one hump and a camel with two? Discord uses `camel` and `dromedary_camel`, but us cowboy's don't know nothing about those, so 'round here, we just use `camel_one_hump` and `camel_two_humps`'. This script isn't a good solution for all problems, but it is meant to get your horse trottin' in the right direction.
