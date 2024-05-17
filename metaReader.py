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

            # Print base image resolution
            base_image_resolution = metadata_dict.get("base_image_resolution", {})
            print(f"Base Image Resolution: {base_image_resolution}")

            # Print image details
            images = metadata_dict.get("images", {})
            for filename, details in images.items():
                trait = details.get("Trait", "Unknown")
                x = details.get("x", "Unknown")
                y = details.get("y", "Unknown")
                print(f"{filename}, Trait: {trait}, Coordinates: (x: {x}, y: {y})")
        else:
            print("No metadata found in the image.")

if __name__ == "__main__":
    base_dir = os.getcwd()
    image_path = os.path.join(base_dir, "stitched_image.png")
    
    read_metadata(image_path)
