import cv2
import numpy as np

def glitch_effect(image_path, output_path, intensity=5):
    image = cv2.imread(image_path)
    rows, cols, _ = image.shape
    for i in range(rows):
        offset = np.random.randint(-intensity, intensity)
        image[i] = np.roll(image[i], offset, axis=0)
    cv2.imwrite(output_path, image)

# Example usage
input_image_path = "/Users/claramalan/Desktop/gradient+fixed+invert+IMG_4481.JPG"
output_image_path = "/Users/claramalan/Desktop/glitch+gradient+fixed+invert+IMG_4481.JPG"
glitch_effect(input_image_path, output_image_path)
