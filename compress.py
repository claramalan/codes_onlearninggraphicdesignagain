import os
from PIL import Image

def compress_image(input_path, output_path, target_size):
    quality = 90
    image = Image.open(input_path)
    image.save(output_path, optimize=True, quality=quality)  # Create the initial file

    while os.path.getsize(output_path) > target_size * 1024 and quality > 0:
        quality -= 5
        image.save(output_path, optimize=True, quality=quality)

input_path = "/Users/claramalan/Desktop/opacity++abstract+glitch+gradient+fixed+invert+IMG_4481.JPG"
output_path = "/Users/claramalan/Desktop/comprsed+invert+IMG_4481.JPG"
target_size = 20  # in KB

compress_image(input_path, output_path, target_size)
