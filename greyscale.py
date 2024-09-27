from PIL import Image

def convert_to_grayscale(image):
    return image.convert("L")

def main():
    # Open an image file
    image_path = "/Users/claramalan/Desktop/ffblurinvertdrawing+isolated_IMG_4194.jpeg"
    image = Image.open(image_path)

    # Convert the image to grayscale
    grayscale_image = convert_to_grayscale(image)

    # Save the grayscale image
    output_path = "/Users/claramalan/Desktop/fgreyffblurinvertdrawing+isolated_IMG_4194.jpeg"
    grayscale_image.save(output_path)
    print(f"Grayscale image saved at: {output_path}")

if __name__ == "__main__":
    main()
