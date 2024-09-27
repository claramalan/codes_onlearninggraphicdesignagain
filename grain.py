import random
from PIL import Image, ImageDraw

def draw_black_and_white_dots(image_path, output_path, num_dots):
    # Open the image
    image = Image.open(image_path)
    
    # Get the dimensions of the original image
    image_width, image_height = image.size
    
    # Create a blank image with the same dimensions as the original image
    result = Image.new("RGB", (image_width, image_height))
    
    # Paste the original image onto the result image
    result.paste(image, (0, 0))
    
    # Create a drawing object
    draw = ImageDraw.Draw(result)
    
    # Draw black dots on the image
    for _ in range(num_dots):
        # Randomly choose the position for each dot
        x = random.randint(0, image_width - 1)
        y = random.randint(0, image_height - 1)
        
        # Draw a black dot at the chosen position
        draw.point((x, y), fill="black")
    
    # Save the modified image
    result.save(output_path)

# Example usage
image_path = '/Users/claramalan/Desktop/IMG_4590 .JPG'
output_path = '/Users/claramalan/Desktop/IMG_4590 .JPG'
num_dots = 963400  # Number of black dots to draw

draw_black_and_white_dots(image_path, output_path, num_dots)
