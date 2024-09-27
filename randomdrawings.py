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
    
    # Draw random drawings with random colors
    for _ in range(num_drawings):
        # Randomly choose the position and size for each drawing
        x1 = random.randint(0, image_width - max_drawing_size)
        y1 = random.randint(0, image_height - max_drawing_size)
        x2 = x1 + random.randint(1, max_drawing_size)
        y2 = y1 + random.randint(1, max_drawing_size)
        
        # Randomly choose the drawing type (lines, curves, etc.)
        drawing_type = random.choice(["line", "curve"])
        
        # Randomly choose the color for the drawing
        color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
        
        # Draw the drawing on the result image
        if drawing_type == "line":
            draw.line([x1, y1, x2, y2], fill=color, width=random.randint(6, 12))
        elif drawing_type == "curve":
            # Example of drawing a curve
            draw.arc([x1, y1, x2, y2], start=random.randint(0, 180), end=random.randint(180, 360), fill=color)
        
    
    # Save the modified image
    result.save(output_path)

# Example usage
image_path = '/Users/claramalan/Desktop/IMG_4590.JPG'
output_path = '/Users/claramalan/Desktop/drawingsIMG_4590.JPG'
num_drawings = 7  # Number of random drawings to draw

draw_random_drawings(image_path, output_path, num_drawings)
