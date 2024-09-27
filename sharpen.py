from PIL import Image, ImageFilter

def sharpen_image(input_path, output_path, radius=2, percent=150, threshold=3):
    # Open the input image
    image = Image.open(input_path)

    # Apply the unsharp mask filter
    sharpened_image = image.filter(ImageFilter.UnsharpMask(radius=radius, percent=percent, threshold=threshold))

    # Save the sharpened image
    sharpened_image.save(output_path)

# Example usage
input_image_path = "/Users/claramalan/Desktop/IMG_4590 -1.JPG"
output_image_path = "/Users/claramalan/Desktop/IMG_4590 -1.JPG"
sharpen_image(input_image_path, output_image_path, radius=5, percent=360, threshold=3)
