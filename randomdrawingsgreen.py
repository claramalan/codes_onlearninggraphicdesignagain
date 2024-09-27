import random
from PIL import Image, ImageDraw

def draw_random_drawings(image_path, output_path, num_drawings):
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
    
    # Define the maximum size for the drawings
    max_drawing_size = min(image_width, image_height) // 2
    
    # Define the color for the drawings (dark green)
    dark_green = (0, 100, 0)
    
    # Draw random drawings with dark green color
    for _ in range(num_drawings):
        # Randomly choose the position and size for each drawing
        x1 = random.randint(0, image_width - max_drawing_size)
        y1 = random.randint(0, image_height - max_drawing_size)
        x2 = x1 + random.randint(1, max_drawing_size)
        y2 = y1 + random.randint(1, max_drawing_size)
        
        # Randomly choose the drawing type (lines, curves, etc.)
        drawing_type = random.choice(["line", "curve"])
        
        # Draw the drawing on the result image
        if drawing_type == "line":
            draw.line([x1, y1, x2, y2], fill=dark_green, width=random.randint(1, 5))
        elif drawing_type == "curve":
            # Example of drawing a curve
            draw.arc([x1, y1, x2, y2], start=random.randint(0, 180), end=random.randint(180, 360), fill=dark_green)
        
    # Save the modified image
    result.save(output_path)

# Example usage
image_path = '/Users/claramalan/Desktop/enhancedIMG_4568.PNG'
output_path = '/Users/claramalan/Desktop/dither+compressIMG_4481.JPG'
num_drawings = 300  # Number of random drawings to draw

draw_random_drawings(image_path, output_path, num_drawings)
