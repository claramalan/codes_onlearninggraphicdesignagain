from PIL import Image, ImageEnhance

def enhance_image_color(input_image_path, output_image_path, enhancement_factor):
    """
    Enhance the color of an image.

    :param input_image_path: Path to the input image
    :param output_image_path: Path to save the enhanced image
    :param enhancement_factor: Factor to enhance the color (1.0 means no change, >1.0 means more color)
    """
    # Open the image
    image = Image.open(input_image_path)
    
    # Enhance the color
    enhancer = ImageEnhance.Color(image)
    enhanced_image = enhancer.enhance(enhancement_factor)
    
    # Save the enhanced image
    enhanced_image.save(output_image_path, "PNG")

# Example usage
input_image_path = "/Users/claramalan/Desktop/IMG_4590.JPG"
output_image_path = "/Users/claramalan/Desktop/enhanceIMG_4590.JPG"
enhancement_factor = 1.4 # Increase the color by 90%

enhance_image_color(input_image_path, output_image_path, enhancement_factor)
