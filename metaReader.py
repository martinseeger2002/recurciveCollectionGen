from PIL import Image, PngImagePlugin
import json
import os

def read_metadata(image_path):
    with Image.open(image_path) as img:
        # Check if the image has metadata
        if "Metadata" in img.info:
            metadata = img.info["Metadata"]
            metadata_dict = json.loads(metadata)
            print("Metadata found in the image:")
            for filename, coords in metadata_dict.items():
                print(f"File: {filename}, Coordinates: {coords}")
        else:
            print("No metadata found in the image.")

if __name__ == "__main__":
    base_dir = os.getcwd()
    image_path = os.path.join(base_dir, "stitched_image.png")
    
    read_metadata(image_path)
