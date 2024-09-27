import cv2
import numpy as np

def draw_shape(img, center, size, shape, color):
    if shape == 'circle':
        cv2.circle(img, center, size, color, -1)
    elif shape == 'square':
        top_left = (center[0] - size, center[1] - size)
        bottom_right = (center[0] + size, center[1] + size)
        cv2.rectangle(img, top_left, bottom_right, color, -1)
    elif shape == 'triangle':
        points = np.array([
            [center[0], center[1] - size],
            [center[0] - size, center[1] + size],
            [center[0] + size, center[1] + size]
        ])
        cv2.drawContours(img, [points], 0, color, -1)

def image_to_dots(image_path, dot_size=5, spacing=10, shape='circle', color=True):
    image = cv2.imread(image_path)
    if image is None:
        print("Error loading image")
        return

    height, width, _ = image.shape
    new_height = height // spacing
    new_width = width // spacing
    resized_image = cv2.resize(image, (new_width, new_height), interpolation=cv2.INTER_AREA)

    dot_image = np.ones((height, width, 1), dtype=np.uint8) * 255

    for y in range(new_height):
        for x in range(new_width):
            if color:
                b, g, r = resized_image[y, x]
                intensity = (r + g + b) / 3
            else:
                gray = cv2.cvtColor(resized_image, cv2.COLOR_BGR2GRAY)
                intensity = gray[y, x]
                b, g, r = (intensity, intensity, intensity)
                
            radius = dot_size * (intensity / 555)
            center = (x * spacing, y * spacing)
            draw_shape(dot_image, center, int(radius), shape, (int(b), int(g), int(r)))

    return dot_image

input_image_path = '/Users/claramalan/Desktop/IMG_4590 .JPG'
output_image_path = '/Users/claramalan/Desktop/dotIMG_4590 .JPG'

dot_image = image_to_dots(input_image_path, dot_size=45, spacing=12, shape='triangle', color=True)
cv2.imwrite(output_image_path, dot_image)
print(f'Dot representation saved to {output_image_path}')
