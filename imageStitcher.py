from PIL import Image, PngImagePlugin
import os
import json

def stitch_images(base_dir, output_path, rows, cols):
    img_size = 1413
    final_img_width = cols * img_size
    final_img_height = rows * img_size

    # Create a new blank image with transparent background
    final_image = Image.new("RGBA", (final_img_width, final_img_height), (0, 0, 0, 0))

    # Metadata dictionary to store coordinates and filenames
    metadata = {}

    # Get all folder paths starting with a number from 1 to the number of rows
    folder_paths = [os.path.join(base_dir, folder) for folder in os.listdir(base_dir) 
                    if folder[0].isdigit() and 1 <= int(folder[0]) <= rows]
    folder_paths.sort(key=lambda x: int(os.path.basename(x)[0]))  # Sort by first character

    for row, folder in enumerate(folder_paths):
        images = [f for f in os.listdir(folder) if f.endswith('.png')]
        images.sort()  # Ensure images are in order

        for col, img_name in enumerate(images):
            if col >= cols:
                break  # Skip images that exceed the column count
            img_path = os.path.join(folder, img_name)
            img = Image.open(img_path).convert("RGBA")
            final_image.paste(img, (col * img_size, row * img_size), img)
            
            # Store the metadata
            metadata[img_name] = {"x": col * img_size, "y": row * img_size}

    # Add metadata to the final image
    meta = PngImagePlugin.PngInfo()
    meta.add_text("Metadata", json.dumps(metadata))

    final_image.save(output_path, format="PNG", pnginfo=meta)
    print(f"Image saved at {output_path} with metadata.")

if __name__ == "__main__":
    base_dir = os.getcwd()
    output_path = os.path.join(base_dir, "stitched_image.png")

    # Define the number of rows and columns for the grid
    rows = 3
    cols = 8
    
    stitch_images(base_dir, output_path, rows, cols)
