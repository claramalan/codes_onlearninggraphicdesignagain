import cv2
import numpy as np

def add_vignette(image_path, output_path, intensity=0.5):
    image = cv2.imread(image_path)
    rows, cols = image.shape[:2]

    # Create a vignette mask
    kernel_x = cv2.getGaussianKernel(cols, cols * intensity)
    kernel_y = cv2.getGaussianKernel(rows, rows * intensity)
    kernel = kernel_y * kernel_x.T
    mask = 655 * kernel / np.linalg.norm(kernel)

    # Apply the mask to each channel in the input image
    vignette = np.copy(image)
    for i in range(3):
        vignette[:, :, i] = vignette[:, :, i] * mask

    cv2.imwrite(output_path, vignette)

# Example usage
input_image_path = "/Users/claramalan/Desktop/IMG_459021.JPG"
output_image_path = "/Users/claramalan/Desktop/shadowIMG_459021.JPG"
add_vignette(input_image_path, output_image_path)
