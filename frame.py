from PIL import Image, ImageOps

def add_frame(image_path, output_path, frame_width=10, color='black'):
    image = Image.open(image_path)
    framed_image = ImageOps.expand(image, border=frame_width, fill=color)
    framed_image.save(output_path)

# Example usage
input_image_path = "/Users/claramalan/Desktop/IMG_459021.JPG"
output_image_path = "/Users/claramalan/Desktop/frameIMG_459021.JPG"
add_frame(input_image_path, output_image_path, frame_width=30, color='red')
