from PIL import Image
import os

def resize_image(input_path, output_path, max_size_kb=20):
    """
    Resize an image to reduce its file size to be less than the specified maximum size in kilobytes.

    Args:
        input_path (str): Path to the input image file.
        output_path (str): Path to save the resized image.
        max_size_kb (int): Maximum allowed file size in kilobytes (default is 20KB).
    """
    try:
        # Open the input image
        with Image.open(input_path) as img:
            # Calculate the target image quality based on the maximum file size
            quality = 95  # Initial quality value
            while True:
                # Save the image with the current quality setting
                img.save(output_path, optimize=True, quality=quality)
                # Check the file size
                file_size_kb = os.path.getsize(output_path) / 1024
                # If the file size is less than or equal to the maximum size, break the loop
                if file_size_kb <= max_size_kb:
                    break
                # Reduce the quality for the next iteration
                quality -= 5
                # Ensure that quality is within valid range (0 to 100)
                quality = max(0, min(quality, 100))
            print(f"Image resized successfully! New file size: {file_size_kb:.2f} KB")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    # Example usage
    input_image_path = "/Users/claramalan/Desktop/Screenshot 2024-03-06 at 14.54.58.png"
    output_image_path = "/Users/claramalan/Desktop/Screenshot 2024-03-06 at 14.54.58output.png"
    max_size_kb = 20  # Maximum allowed file size in kilobytes (20KB)
    resize_image(input_image_path, output_image_path, max_size_kb)
