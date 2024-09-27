import cv2
import numpy as np

def tilt_shift(image_path, output_path, focus_center, focus_radius, blur_strength=20):
    image = cv2.imread(image_path)
    height, width = image.shape[:2]
    
    mask = np.zeros((height, width), dtype=np.uint8)
    cv2.circle(mask, focus_center, focus_radius, 255, -3)
    
    # Apply Gaussian blur to the image
    blurred = cv2.GaussianBlur(image, (0, 0), blur_strength)
    
    # Blend the blurred image with the original image using the mask
    result = cv2.bitwise_and(blurred, blurred, mask=cv2.bitwise_not(mask))
    result += cv2.bitwise_and(image, image, mask=mask)
    
    cv2.imwrite(output_path, result)

# Example usage
input_image_path = "/Users/claramalan/Desktop/IMG_451.JPG"
output_image_path = "/Users/claramalan/Desktop/tilshiftIMG_451.JPG"
tilt_shift(input_image_path, output_image_path, focus_center=(20, 300), focus_radius=50)
