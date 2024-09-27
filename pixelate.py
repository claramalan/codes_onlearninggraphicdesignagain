from PIL import Image

def pixelate(image_path, output_path, pixel_size=17):
    image = Image.open(image_path)
    image = image.resize(
        (image.size[0] // pixel_size, image.size[1] // pixel_size),
        resample=Image.NEAREST
    )
    image = image.resize(
        (image.size[0] * pixel_size, image.size[1] * pixel_size),
        resample=Image.NEAREST
    )
    image.save(output_path)

# Example usage
input_image_path = "//Users/claramalan/Desktop/IMG_459021.JPG"
output_image_path = "/Users/claramalan/Desktop/pIMG_459021.JPG"
pixelate(input_image_path, output_image_path)
