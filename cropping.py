from PIL import Image

def crop_image(file_path, left, top, right, bottom):
    with Image.open(file_path) as img:
        # Define the area to be cropped (in pixels)
        # (left, upper, right, lower)
        area = (left, top, right, bottom)

        # Crop the image
        cropped_img = img.crop(area)

        # Save the cropped image with a new file name
        new_file_path = f"cropped_{file_path.split('/')[-1]}"
        cropped_img.save(new_file_path)

        # Return the new file path
        return new_file_path

# Use the function and print the new file path
image_path = "/Users/claramalan/Desktop/antenna Try out.png"
new_image_path = crop_image(image_path, 10, 70, 200, 200)
print(f"New image saved at: {new_image_path}")
