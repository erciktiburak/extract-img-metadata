from PIL import Image
import os

def extract_metadata(image_path):
    # Open the image file
    with Image.open(image_path) as img:
        # Get basic information
        format = img.format
        size = img.size
        mode = img.mode

        # Get additional metadata
        metadata = img.info

    # Display the metadata
    print(f"Image Format: {format}")
    print(f"Image Size: {size}")
    print(f"Image Mode: {mode}")
    print("Additional Metadata:")
    for key, value in metadata.items():
        print(f"{key}: {value}")

# Path to the image file
image_path = "123.jpg"

# Check if the file exists
if os.path.exists(image_path):
    # Extract and display metadata
    extract_metadata(image_path)
else:
    print("Image file not found.")
