import random
import math
from PIL import Image, ImageDraw

def draw_black_dots_on_shape(image_path, output_path, num_dots, dot_size):
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
    
    # Generate a random shape
    shape = generate_random_shape(image_width, image_height)
    
    # Draw black dots along the random shape
    for _ in range(num_dots):
        # Randomly choose a point along the shape
        x, y = random.choice(shape)
        
        # Draw a black dot at the chosen point
        draw.rectangle([(x - dot_size // 2, y - dot_size // 2), (x + dot_size // 2, y + dot_size // 2)], fill="black")
    
    # Save the modified image
    result.save(output_path)

def generate_random_shape(width, height):
    # Generate a random number of vertices for the shape
    num_vertices = random.randint(3, 10)
    
    # Generate random coordinates for each vertex
    vertices = [(random.randint(0, width - 1), random.randint(0, height - 1)) for _ in range(num_vertices)]
    
    # Sort the vertices based on their x-coordinate
    vertices.sort(key=lambda vertex: vertex[0])
    
    # Connect the vertices to form the shape
    shape = []
    for i in range(len(vertices)):
        x1, y1 = vertices[i]
        x2, y2 = vertices[(i + 1) % len(vertices)]
        
        # Use Bresenham's line algorithm to draw a line between the vertices
        points = bresenham_line(x1, y1, x2, y2)
        shape.extend(points)
    
    return shape

def bresenham_line(x1, y1, x2, y2):
    points = []
    dx = abs(x2 - x1)
    dy = abs(y2 - y1)
    sx = -1 if x1 > x2 else 1
    sy = -1 if y1 > y2 else 1
    err = dx - dy
    
    while True:
        points.append((x1, y1))
        
        if x1 == x2 and y1 == y2:
            break
        
        e2 = 2 * err
        if e2 > -dy:
            err -= dy
            x1 += sx
        if e2 < dx:
            err += dx
            y1 += sy
    
    return points

# Example usage
image_path = '/Users/claramalan/Desktop/IMG_4590 .JPG'
output_path = '/Users/claramalan/Desktop/dotsIMG_4590 .JPG'
num_dots = 900  # Number of black dots to draw
dot_size = 46  # Size of the dots

draw_black_dots_on_shape(image_path, output_path, num_dots, dot_size)
