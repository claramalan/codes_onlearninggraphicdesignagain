from PIL import Image

def dither_image(input_image_path, output_image_path):
    # Open the input image
    image = Image.open(input_image_path)

    # Convert the image to grayscale
    image = image.convert('L')

    # Apply Floyd-Steinberg dithering
    image = image.convert('1', dither=Image.FLOYDSTEINBERG)

    # Save the dithered image
    image.save(output_image_path)

# Example usage
input_image_path = '/Users/claramalan/Desktop/IMG_4590.JPG'
output_image_path = '/Users/claramalan/Desktop/ditherIMG_4590.JPG'
dither_image(input_image_path, output_image_path)
