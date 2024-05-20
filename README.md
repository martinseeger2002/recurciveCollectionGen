
# Image Stitching and Metadata Handling

This repository contains two Python scripts:

1. `imageStitcher.py`: Stitches images from multiple folders into an 8x8 grid and includes metadata.
2. `metaReader.py`: Reads and prints metadata from the stitched image.

## Requirements

- Python 3.x
- Pillow library

You can install the Pillow library using pip:

```bash
pip install pillow
```

## Usage

imageStitcher.py and metaReader.py is for images with no # rarity index

imageStitcherV2.py and metaReaderV2.py is for images with # rarity index

### Stitch Images with Metadata

The `imageStitcher.py` script stitches images from folders named the number of rows (or any folder with names starting with these digits) into a grid and saves the resulting image with metadata.

1. Ensure your working directory contains the folders named the number of rows with the images. The first character of each folder name is used to determine the row in which the images should be placed. (eg. /1Background, /2Body, /3face)
2. Run the script:

```bash
python imageStitcher.py
```

The script will create a `stitched_image.png` file in the same directory with metadata containing the coordinates and filenames of the images used.

### Add Stitched Image to parent script.

After stitching the images and generating the stitched_image.png with metadata, you need to incorporate this image in base64 format into the parent script sketch.js and create the child HTMLs for inscription.

Convert Stitched Image to Base64
Convert the stitched_image.png to a base64 string. You can use online tools or a script to do this.

Add Base64 Image to Parent Script
Open the parentScript.js and replace <Your Stitched Image in base64> with the copied base64 string.

Replace <YourStitchedImageJSInscriptionID> with the inscription ID of the parent script containing the base64 image.

Save the child index.html file. Inscribe the child index.html

### Read and Print Metadata

The `metaReadder.py` script reads and prints the metadata from the `stitched_image.png` file.

1. Ensure `stitched_image.png` is in your working directory.
2. Run the script:

```bash
python metaReader.py
```

The script will print the metadata, showing the trait type, trait name, and their coordinates.



## License

This project is licensed under the MIT License
