import cv2
import numpy as np

def bokeh_effect(image_path, output_path, radius=21, threshold=50):
    image = cv2.imread(image_path)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    
    # Detect edges using Canny
    edges = cv2.Canny(gray, threshold, threshold * 4)
    
    # Create a mask of the edges
    mask = cv2.dilate(edges, None, iterations=2)
    mask = cv2.GaussianBlur(mask, (radius, radius), 0)
    
    # Invert mask
    mask_inv = cv2.bitwise_not(mask)
    
    # Blur the entire image
    blurred = cv2.GaussianBlur(image, (radius, radius), 0)
    
    # Combine the original image and the blurred image using the mask
    bokeh_image = cv2.bitwise_and(image, image, mask=mask) + cv2.bitwise_and(blurred, blurred, mask=mask_inv)
    
    cv2.imwrite(output_path, bokeh_image)

# Example usage
input_image_path = "/Users/claramalan/Desktop/IMG_459021.JPG"
output_image_path = "/Users/claramalan/Desktop/bokehIMG_459021.JPG"
bokeh_effect(input_image_path, output_image_path, radius=21, threshold=50)
