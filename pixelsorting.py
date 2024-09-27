import cv2
import numpy as np

def pixel_sort(image_path, output_path):
    image = cv2.imread(image_path)
    sorted_image = np.zeros_like(image)
    
    for i in range(image.shape[0]):
        row = image[i, :, :]
        row_sorted = row[np.argsort(row[:, 2])]
        sorted_image[i, :, :] = row_sorted
    
    cv2.imwrite(output_path, sorted_image)

# Example usage
input_image_path = "/Users/claramalan/Desktop/Screenshot 2024-09-13 at 12.11.11.png"
output_image_path = "/Users/claramalan/Desktop/Screenshottryout22.11.11.png"
pixel_sort(input_image_path, output_image_path)
