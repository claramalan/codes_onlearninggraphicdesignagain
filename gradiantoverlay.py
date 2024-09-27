import cv2
import numpy as np

def gradient_map(image_path, output_path, color1, color2):
    image = cv2.imread(image_path)
    gradient = np.linspace(color1, color2, 256).astype(np.uint8)
    lut = np.zeros((256, 1, 3), dtype=np.uint8)
    
    for i in range(256):
        lut[i, 0, :] = gradient[i]
    
    gradient_mapped = cv2.LUT(image, lut)
    cv2.imwrite(output_path, gradient_mapped)

# Example usage
input_image_path = "/Users/claramalan/Desktop/IMG_459021.JPG"
output_image_path = "/Users/claramalan/Desktop/gradiantIMG_459021.JPG"
color1 = [165, 42, 42]  # Brown
color2 = [128, 128, 128]  # Grey
gradient_map(input_image_path, output_image_path, color1, color2)
