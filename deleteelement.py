import cv2
import numpy as np

def remove_main_element(input_image_path, output_image_path):
    # Read the image
    image = cv2.imread(input_image_path)

    # Create a mask and initialize it with zeros
    mask = np.zeros(image.shape[:2], np.uint8)

    # Set the background and foreground models
    bgd_model = np.zeros((1, 65), np.float64)
    fgd_model = np.zeros((1, 65), np.float64)

    # Define the rectangle enclosing the main object
    height, width = image.shape[:2]
    rect = (50, 50, width - 50, height - 50)  # Adjust these coordinates as needed

    # Apply GrabCut algorithm to segment the main object
    cv2.grabCut(image, mask, rect, bgd_model, fgd_model, 5, cv2.GC_INIT_WITH_RECT)

    # Create a mask where all probable foreground and definite foreground pixels are marked as 1
    mask2 = np.where((mask == 2) | (mask == 0), 0, 1).astype('uint8')

    # Multiply the original image with the mask to remove the main object
    result = image * mask2[:, :, np.newaxis]

    # Save the resulting image
    cv2.imwrite(output_image_path, result)

# Example usage
input_image_path = '/Users/claramalan/Desktop/IMG_4590.JPG'
output_image_path = '/Users/claramalan/Desktop/deletelementsIMG_4590.JPG'
remove_main_element(input_image_path, output_image_path)
