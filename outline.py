import cv2
import numpy as np

def outline_effect(image_path, output_path):
    image = cv2.imread(image_path)
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    edges = cv2.Canny(gray_image, 100, 500)
    
    # Create a color version of the edges
    edges_colored = cv2.cvtColor(edges, cv2.COLOR_GRAY2BGR)
    
    # Blend the edges with the original image
    outlined_image = cv2.addWeighted(image, 0.9, edges_colored, 6.9, 17)
    
    cv2.imwrite(output_path, outlined_image)

# Example usage
input_image_path = "/Users/claramalan/Desktop/IMG_459021.JPG"
output_image_path = "/Users/claramalan/Desktop/outlineIMG_459021.JPG"
outline_effect(input_image_path, output_image_path)
