from PIL import Image

def change_opacity(input_image_path, output_image_path, opacity):
    """
    Change the opacity of an image.

    :param input_image_path: Path to the input image
    :param output_image_path: Path to save the modified image
    :param opacity: Opacity level (0 to 255)
    """
    # Open the image
    image = Image.open(input_image_path).convert("RGBA")
    
    # Split the image into its components
    r, g, b, a = image.split()
    
    # Apply the opacity to the alpha channel
    a = a.point(lambda p: p * opacity / 255)
    
    # Merge the channels back
    image.putalpha(a)
    
    # Save the image
    image.save(output_image_path, "PNG")

# Example usage
input_image_path = "/Users/claramalan/Desktop/IMG_4590.JPG"
output_image_path = "/Users/claramalan/Desktop/opacityIMG_4590.JPG"
opacity = 180  # Set the desired opacity level (0 to 255)

change_opacity(input_image_path, output_image_path, opacity)
