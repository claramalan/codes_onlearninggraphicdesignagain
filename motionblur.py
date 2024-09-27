import cv2
import numpy as np

def motion_blur(image_path, output_path, size=775):
    image = cv2.imread(image_path)
    
    # Create the motion blur kernel
    kernel = np.zeros((size, size))
    kernel[int((size - 1)/2), :] = np.ones(size)
    kernel = kernel / size
    
    # Apply the kernel to the image
    motion_blur_image = cv2.filter2D(image, -1, kernel)
    
    cv2.imwrite(output_path, motion_blur_image)

# Example usage
input_image_path = "/Users/claramalan/Desktop/IMG_459021.JPG"
output_image_path = "/Users/claramalan/Desktop/motionblurIMG_459021.JPG"
motion_blur(input_image_path, output_image_path, size=70)
