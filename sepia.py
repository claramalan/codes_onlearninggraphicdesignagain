import os
from PIL import Image

def apply_sepia(input_file_path, output_file_path):
    # Check if the input image file exists
    if not os.path.exists(input_file_path):
        print(f"Error: Input file '{input_file_path}' does not exist.")
        return

    with Image.open(input_file_path) as image:
        width, height = image.size
        sepia_data = []
        for y in range(height):
            for x in range(width):
                r, g, b = image.getpixel((x, y))[:3]  # Only take the first three channels
                tr = int(0.393 * r + 0.769 * g + 0.189 * b)
                tg = int(0.349 * r + 0.686 * g + 0.168 * b)
                tb = int(0.272 * r + 0.534 * g + 0.131 * b)
                sepia_data.append((tr, tg, tb))
        sepia_image = Image.new("RGB", (width, height))
        sepia_image.putdata(sepia_data)
        sepia_image.save(output_file_path)
        print(f"Sepia image saved at: {output_file_path}")

# Use the function
input_file_path = "/Users/claramalan/Desktop/IMG_4590.JPG"
output_file_path = "/Users/claramalan/Desktop/sepiaIMG_4590.JPG"
apply_sepia(input_file_path, output_file_path)
