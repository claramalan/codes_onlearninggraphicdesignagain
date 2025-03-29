from PIL import Image
import os

def collage_style(images, output_path, rows=3, cols=3, padding=10, target_size=None):
    """
    Create a collage from multiple images with padding and optional resizing.
    
    Args:
        images (list): List of image file paths
        output_path (str): Path where the collage will be saved
        rows (int): Number of rows in the collage
        cols (int): Number of columns in the collage
        padding (int): Padding between images in pixels
        target_size (tuple): Optional target size for each image (width, height)
    """
    try:
        # Open and process all input images
        input_images = []
        for image_path in images:
            if not os.path.exists(image_path):
                raise FileNotFoundError(f"Image not found: {image_path}")
            
            img = Image.open(image_path)
            # Convert to RGB if necessary
            if img.mode != 'RGB':
                img = img.convert('RGB')
            
            # Resize if target size is specified
            if target_size:
                img = img.resize(target_size, Image.Resampling.LANCZOS)
            
            input_images.append(img)

        # Calculate canvas size
        max_width = max(img.width for img in input_images)
        max_height = max(img.height for img in input_images)
        
        canvas_width = (max_width * cols) + (padding * (cols + 1))
        canvas_height = (max_height * rows) + (padding * (rows + 1))

        # Create a blank canvas for the collage
        collage = Image.new("RGB", (canvas_width, canvas_height), (255, 255, 255))

        # Paste images onto the canvas with padding
        for i, image in enumerate(input_images):
            row = i // cols
            col = i % cols
            x_offset = (col * max_width) + (padding * (col + 1))
            y_offset = (row * max_height) + (padding * (row + 1))
            collage.paste(image, (x_offset, y_offset))

        # Save the collage
        collage.save(output_path, quality=95)
        return True

    except Exception as e:
        print(f"Error creating collage: {str(e)}")
        return False

# Example usage
if __name__ == "__main__":
    # Example with relative paths and target size
    input_images = [
        "path/to/image1.jpg",
        "path/to/image2.jpg",
        "path/to/image3.jpg",
        "path/to/image4.jpg"
    ]
    
    # Create a 2x2 collage with 20px padding and 400x400 image size
    output_path = "output_collage.jpg"
    success = collage_style(
        input_images,
        output_path,
        rows=2,
        cols=2,
        padding=20,
        target_size=(400, 400)
    )
    
    if success:
        print(f"Collage created successfully at: {output_path}")
    else:
        print("Failed to create collage")
