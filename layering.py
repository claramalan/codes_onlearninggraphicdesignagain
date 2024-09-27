import cv2
import numpy as np
from PIL import Image

# Load the base image and the overlay image
base_image_path = '/Users/claramalan/Desktop/untitled folder 2/antenna_code/BLURgradiantoverlayantenna Try out.png'
overlay_image_path = '/Users/claramalan/Desktop/untitled folder 2/antenna_code/dotimage3_antenna Try out.png'  # Replace with your overlay image path

# Load images using OpenCV
base_image = cv2.imread(base_image_path, cv2.IMREAD_COLOR)
overlay_image = cv2.imread(overlay_image_path, cv2.IMREAD_COLOR)

# Resize overlay image to match base image size
overlay_image = cv2.resize(overlay_image, (base_image.shape[1], base_image.shape[0]))

# Ensure both images have the same number of channels
if base_image.shape[2] != overlay_image.shape[2]:
    # Convert both images to 3 channels (RGB)
    if base_image.shape[2] == 1:
        base_image = cv2.cvtColor(base_image, cv2.COLOR_GRAY2BGR)
    if overlay_image.shape[2] == 1:
        overlay_image = cv2.cvtColor(overlay_image, cv2.COLOR_GRAY2BGR)

# Convert images to float for blending
base_image = base_image.astype(float)
overlay_image = overlay_image.astype(float)

# Blend images with transparency (alpha blending)
alpha = 0.5  # Transparency factor for overlay image
blended_image = cv2.addWeighted(base_image, 1 - alpha, overlay_image, alpha, 0)

# Convert back to uint8
blended_image = blended_image.astype(np.uint8)

# Save the blended image
output_path = '/Users/claramalan/Desktop/layerIMG_4590 .JPG'
cv2.imwrite(output_path, blended_image)

# Display the result using PIL
Image.fromarray(cv2.cvtColor(blended_image, cv2.COLOR_BGR2RGB)).show()
