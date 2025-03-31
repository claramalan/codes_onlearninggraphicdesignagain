from PIL import Image
import numpy as np

def separate_colors_to_pdf(input_image_path, output_folder, dpi=300, margin_mm=5):
    # Open the image
    img = Image.open(input_image_path)

    # Convert image to RGB if it's not in RGB mode
    if img.mode != "RGB":
        img = img.convert("RGB")

    # Convert margin from mm to pixels based on DPI
    margin_px = int(margin_mm / 25.4 * dpi)

    # Extract the Red, Green, and Blue channels as NumPy arrays
    red_channel, green_channel, blue_channel = img.split()

    # Convert channels to NumPy arrays for manipulation
    red_array = np.array(red_channel)
    green_array = np.array(green_channel)
    blue_array = np.array(blue_channel)

    # Create distinct grayscale layers by zeroing out other channels
    red_only = np.where((red_array >= green_array) & (red_array >= blue_array), red_array, 255)
    green_only = np.where((green_array >= red_array) & (green_array >= blue_array), green_array, 255)
    blue_only = np.where((blue_array >= red_array) & (blue_array >= green_array), blue_array, 255)

    # Convert the NumPy arrays back to PIL Images
    red_layer = Image.fromarray(red_only).convert("L")
    green_layer = Image.fromarray(green_only).convert("L")
    blue_layer = Image.fromarray(blue_only).convert("L")

    # Process each channel with margin and save as separate PDFs
    channels = [("red", red_layer), ("green", green_layer), ("blue", blue_layer)]

    for color_name, channel_image in channels:
        # Create new image with margin
        new_width = channel_image.width + 2 * margin_px
        new_height = channel_image.height + 2 * margin_px

        # Create a new grayscale image with white background (for margin)
        img_with_margin = Image.new("L", (new_width, new_height), "white")
        img_with_margin.paste(channel_image, (margin_px, margin_px))

        # Save as high-quality PDF with the specified DPI
        output_path = f"{output_folder}/{color_name}_layer.pdf"
        img_with_margin.save(output_path, "PDF", resolution=dpi)

    print(f"Color-separated PDFs saved in {output_folder}")

# Example usage
input_path = "/Users/claramalan/Desktop/tag2.jpg"  # Change to your image path
output_folder = "/Users/claramalan/Desktop"  # Change to your desired output folder
separate_colors_to_pdf(input_path, output_folder, dpi=300)
