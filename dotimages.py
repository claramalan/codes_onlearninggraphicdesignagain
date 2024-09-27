import cv2
import numpy as np

def image_to_dots(image_path, dot_size=5, spacing=10):
    # Load the image
    image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
    if image is None:
        print("Error loading image")
        return

    # Resize image to a smaller size for simplicity
    height, width = image.shape
    new_height = height // spacing
    new_width = width // spacing
    resized_image = cv2.resize(image, (new_width, new_height), interpolation=cv2.INTER_AREA)

    # Create a blank canvas
    dot_image = np.ones((height, width), dtype=np.uint8) * 255

    # Draw dots
    for y in range(new_height):
        for x in range(new_width):
            intensity = resized_image[y, x]
            radius = dot_size * (intensity / 255)
            cv2.circle(dot_image, (x * spacing, y * spacing), int(radius), (0, 0, 0), -1)

    return dot_image

# Example usage
input_image_path = '/Users/claramalan/Desktop/IMG_4590 .JPG'
output_image_path = '/Users/claramalan/Desktop/dotv1IMG_4590 .JPG'

dot_image = image_to_dots(input_image_path)
cv2.imwrite(output_image_path, dot_image)
print(f'Dot representation saved to {output_image_path}')
