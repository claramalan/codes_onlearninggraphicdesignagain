from PIL import Image
import random

def cut_and_rearrange(image_path, output_image_path, num_rows, num_cols):
    # Open the image
    img = Image.open(image_path)
    
    # Get the dimensions of each tile
    width, height = img.size
    tile_width = width // num_cols
    tile_height = height // num_rows
    
    # Create a list to store rearranged tiles
    tiles = []
    
    # Cut the image into tiles
    for y in range(num_rows):
        for x in range(num_cols):
            # Crop each tile
            left = x * tile_width
            upper = y * tile_height
            right = left + tile_width
            lower = upper + tile_height
            tile = img.crop((left, upper, right, lower))
            
            # Append the tile to the list
            tiles.append(tile)
    
    # Shuffle the list of tiles
    random.shuffle(tiles)
    
    # Create a new image by pasting the rearranged tiles
    rearranged_img = Image.new('RGB', (width, height))
    for i, tile in enumerate(tiles):
        x = (i % num_cols) * tile_width
        y = (i // num_cols) * tile_height
        rearranged_img.paste(tile, (x, y))
    
    # Save the rearranged image
    rearranged_img.save(output_image_path)

# Example usage
input_image_path = '/Users/claramalan/Desktop/IMG_4590.JPG'
output_image_path = '/Users/claramalan/Desktop/rearrangeIMG_4590.png'
num_rows = 18
num_cols = 20
cut_and_rearrange(input_image_path, output_image_path, num_rows, num_cols)
