from PIL import Image, ImageEnhance

def increase_luminosity(image_path, output_path, factor):
    # Open the image
    image = Image.open(image_path)
    
    # Create an enhancer object for brightness
    enhancer = ImageEnhance.Brightness(image)
    
    # Increase the brightness by the given factor
    image_enhanced = enhancer.enhance(factor)
    
    # Save the enhanced image
    image_enhanced.save(output_path)

# Example usage
image_path = '/Users/claramalan/Desktop/prints/livelayerblurinvertdrawing+isolated_IMG_4194.jpeg'
output_path = '/Users/claramalan/Desktop/prints/luminotuivelayerblurinvertdrawing+isolated_IMG_4194.jpeg'
luminosity_factor = 1.5 # Factor to increase brightness; >1 increases, <1 decreases

increase_luminosity(image_path, output_path, luminosity_factor)
