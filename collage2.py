from PIL import Image

def collage_style(images, output_path, rows=3, cols=3):
    # Open all input images
    input_images = [Image.open(image) for image in images]

    # Calculate canvas size based on the number of rows and columns
    canvas_width = max(image.width for image in input_images) * cols
    canvas_height = max(image.height for image in input_images) * rows

    # Create a blank canvas for the collage
    collage = Image.new("RGB", (canvas_width, canvas_height), (255, 255, 255))

    # Paste images onto the canvas
    for i, image in enumerate(input_images):
        row = i // cols
        col = i % cols
        x_offset = col * image.width
        y_offset = row * image.height
        collage.paste(image, (x_offset, y_offset))

    # Save the collage
    collage.save(output_path)

# Example usage
input_images = ["/Users/claramalan/Desktop/dotIMG_4590 .JPG", "/Users/claramalan/Desktop/pooooIMG_459021.JPG", "/Users/claramalan/Desktop/transpIMG_4590.png","/Users/claramalan/Desktop/rearrangeIMG_4590.png"]
output_image_path = "/Users/claramalan/Desktop/COLLAGE_IMG_4579.JPG"
collage_style(input_images, output_image_path, rows=2, cols=2)