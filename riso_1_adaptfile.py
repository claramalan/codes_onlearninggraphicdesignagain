from PIL import Image

def convert_to_grayscale_pdf(input_image_path, output_pdf_path, dpi=300, margin_mm=5):
    # Open the image
    img = Image.open(input_image_path)

    # Convert to grayscale
    img_gray = img.convert("L")

    # Calculate pixel size for the margin
    # DPI (dots per inch) to margin pixels conversion (1 inch = 25.4 mm)
    margin_px = int(margin_mm * dpi / 25.4)

    # Create a new image with extra space for the margin
    new_width = img_gray.width + 2 * margin_px
    new_height = img_gray.height + 2 * margin_px

    # Create a new grayscale image with a white background
    img_with_margin = Image.new("L", (new_width, new_height), "white")
    
    # Paste the original grayscale image in the center of the new image
    img_with_margin.paste(img_gray, (margin_px, margin_px))

    # Save the image as a PDF with high resolution
    img_with_margin.save(output_pdf_path, "PDF", resolution=dpi)

# Example usage
input_path = "/Users/claramalan/Desktop/yooooooo.jpg"  # Use your input file path
output_path = "/Users/claramalan/Desktop/yooooooo.pdf"  # Desired output PDF path
convert_to_grayscale_pdf(input_path, output_path, dpi=300)
