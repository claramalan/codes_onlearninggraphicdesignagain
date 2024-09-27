import cv2
import numpy as np

def displacement_map(image_path, map_path, output_path, scale=10):
    image = cv2.imread(image_path)
    displacement = cv2.imread(map_path, cv2.IMREAD_GRAYSCALE)
    
    height, width = image.shape[:2]
    map_x, map_y = np.meshgrid(np.arange(width), np.arange(height))
    
    displacement = cv2.resize(displacement, (width, height)).astype(np.float32)
    
    map_x = (map_x + (displacement - 128) / 128 * scale).astype(np.float32)
    map_y = (map_y + (displacement - 128) / 128 * scale).astype(np.float32)
    
    displaced_image = cv2.remap(image, map_x, map_y, interpolation=cv2.INTER_LINEAR)
    
    cv2.imwrite(output_path, displaced_image)

# Example usage
input_image_path = "/Users/claramalan/Desktop/IMG_451.JPG"
map_image_path = "/Users/claramalan/Desktop/dotIMG_4590 .JPG"
output_image_path = "/Users/claramalan/Desktop/mapapixelateIMG_459021.JPG"
displacement_map(input_image_path, map_image_path, output_image_path, scale=100)
