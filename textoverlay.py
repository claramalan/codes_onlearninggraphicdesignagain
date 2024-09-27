from PIL import Image, ImageDraw, ImageFont

def text_overlay(image_path, output_path, text, font_path="arial.ttf", font_size=150, color=(255, 255, 255, 255)):
    # Open the input image and convert it to RGBA
    image = Image.open(image_path).convert("RGBA")
    txt = Image.new("RGBA", image.size, (255, 255, 255, 0))
    
    # Try to load the specified font, fall back to a default font if not found
    try:
        font = ImageFont.truetype(font_path, font_size)
    except IOError:
        font = ImageFont.load_default()
    
    draw = ImageDraw.Draw(txt)
    
    # Calculate text size and position to center it
    text_width, text_height = draw.textsize(text, font=font)
    position = ((image.width - text_width) // 2, (image.height - text_height) // 2)
    
    # Draw the text onto the transparent layer
    draw.text(position, text, font=font, fill=color)
    
    # Composite the text image onto the original image
    combined = Image.alpha_composite(image, txt)
    
    # Check if the output file extension requires conversion to RGB
    if output_path.lower().endswith('.jpg') or output_path.lower().endswith('.jpeg'):
        combined = combined.convert("RGB")  # Remove alpha for JPEG
    
    # Save the combined image
    combined.save(output_path)

# Example usage
input_image_path = "/Users/claramalan/Desktop/antenna Try out.png"
output_image_path = "/Users/claramalan/Desktop/textoverlayantenna Try out.png"
text_overlay(input_image_path, output_image_path, "Sample Text", font_size=150, color=(255, 255, 255, 255))
