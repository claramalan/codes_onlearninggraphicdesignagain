from PIL import Image, ImageFilter

def blur_image(input_path, output_path, radius=2):
    # Open the input image
    image = Image.open(input_path)

    # Apply the blur filter
    blurred_image = image.filter(ImageFilter.GaussianBlur(radius))

    # Save the blurred image
    blurred_image.save(output_path)

# Example usage
input_image_path = "/Users/claramalan/Desktop/IMG_4590 .JPG"
output_image_path = "/Users/claramalan/Desktop/IMG_4590 .JPG"
blur_image(input_image_path, output_image_path, radius=90)
