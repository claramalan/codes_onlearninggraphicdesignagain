from PIL import Image

def convert_to_bw(image_path, output_path):
    # Open the image
    image = Image.open(image_path)
    
    # Convert the image to grayscale
    bw_image = image.convert('L')
    
    # Save the black and white image
    bw_image.save(output_path)
    
    print("Image converted to black and white.")

# Example usage:
input_image_path = "/Users/claramalan/Desktop/IMG_4590.JPG"
output_image_path = "/Users/claramalan/Desktop/blackandwhiteIMG_4590.JPG"
convert_to_bw(input_image_path, output_image_path)
