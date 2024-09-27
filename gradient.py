import cv2
import numpy as np

def gradient_overlay(image_path, output_path, color1, color2):
    image = cv2.imread(image_path)
    overlay = np.zeros_like(image, dtype=np.uint8)

    rows, cols = overlay.shape[:2]
    for i in range(rows):
        alpha = i / rows
        color = (int(color1[0] * (1 - alpha) + color2[0] * alpha),
                 int(color1[1] * (1 - alpha) + color2[1] * alpha),
                 int(color1[2] * (1 - alpha) + color2[2] * alpha))
        overlay[i, :] = color

    blended = cv2.addWeighted(image, 0.5, overlay, 0.5, 0)
    cv2.imwrite(output_path, blended)

# Example usage
input_image_path = "/Users/claramalan/Desktop/IMG_459021.JPG"
output_image_path = "/Users/claramalan/Desktop/graadiantIMG_459021.JPG"

# Brown to Grey gradient
color_brown = [150, 75, 0]  # BGR for brown
color_grey = [128, 128, 128]  # BGR for grey

gradient_overlay(input_image_path, output_image_path, color_brown, color_grey)
