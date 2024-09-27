from PIL import Image, ImageDraw, ImageOps

def halftone_effect(image_path, output_path, dot_size=5):
    image = Image.open(image_path).convert("L")
    image = ImageOps.invert(image)
    width, height = image.size
    
    halftone = Image.new("L", image.size, 255)
    draw = ImageDraw.Draw(halftone)
    
    for x in range(0, width, dot_size):
        for y in range(0, height, dot_size):
            box = image.crop((x, y, x + dot_size, y + dot_size))
            average = int(box.getextrema()[1])
            radius = (255 - average) // 16 #moify the number to get various results
            draw.ellipse([(x, y), (x + radius, y + radius)], fill=0)
    
    halftone.save(output_path)

# Example usage
input_image_path = "/Users/claramalan/Desktop/IMG_4590 .JPG"
output_image_path = "/Users/claramalan/Desktop/dotIMG_4590 .JPG"
halftone_effect(input_image_path, output_image_path, dot_size=10)
