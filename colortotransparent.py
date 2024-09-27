import cv2
import numpy as np

# Load image
image = cv2.imread('/Users/claramalan/Desktop/IMG_4590.JPG')
if image is None:
    print("Error: Image not loaded properly.")
else:
    # Convert image to HSV color space
    hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

    # Define lower and upper bounds for the color blue in HSV
    lower_blue = np.array([100, 150, 0])
    upper_blue = np.array([140, 255, 255])
    
    # Define lower and upper bounds for the color green in HSV
    lower_green = np.array([40, 40, 40])
    upper_green = np.array([80, 255, 255])

    # Threshold the HSV image to get only the blue and green colors
    mask_blue = cv2.inRange(hsv, lower_blue, upper_blue)
    mask_green = cv2.inRange(hsv, lower_green, upper_green)
    
    # Combine the masks
    mask = cv2.bitwise_or(mask_blue, mask_green)

    # Create a mask for the transparency channel (alpha channel)
    alpha = np.ones_like(image[:, :, 0], dtype=np.uint8) * 255

    # Set the alpha channel of the detected blue and green color pixels to zero, making them transparent
    alpha[mask == 255] = 0

    # Add the alpha channel to the original BGR image
    bgr_with_alpha = cv2.merge((image[:, :, 0], image[:, :, 1], image[:, :, 2], alpha))

    # Save the modified image to an output file (use PNG to preserve alpha channel)
    output_file_path = '/Users/claramalan/Desktop/transpIMG_4590.png'
    cv2.imwrite(output_file_path, bgr_with_alpha)

    print("Output image saved successfully.")
