import os
import sys
from PIL import Image

def convert_images_to_pdf(image_paths, output_pdf_path):
    """
    Converts one or more image files into a single PDF file.
    """
    pil_images = []
    for path in image_paths:
        if not os.path.isfile(path):
            print(f"Warning: File not found at '{path}', skipping.")
            continue
        try:
            image = Image.open(path)
            # Convert RGBA to RGB if necessary, as PDF doesn't support alpha channel well
            if image.mode == 'RGBA':
                image = image.convert('RGB')
            pil_images.append(image)
        except Exception as e:
            print(f"Warning: Could not open or process '{path}': {e}, skipping.")
    
    if not pil_images:
        print("Error: No valid images found to convert.")
        sys.exit(1)
        
    try:
        # The first image is saved, others are appended
        pil_images[0].save(
            output_pdf_path,
            "PDF",
            resolution=100.0,
            save_all=True,
            append_images=pil_images[1:]
        )
        print(f"✅ Successfully converted {len(pil_images)} image(s) to '{output_pdf_path}'")
    except Exception as e:
        print(f"❌ An error occurred during PDF creation: {e}")
        sys.exit(1)

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python image_to_pdf.py <image1_path> [<image2_path> ...]")
        print("\n- If one image is provided, the PDF will be saved with the same name (e.g., 'image.jpg' -> 'image.pdf').")
        print("- If multiple images are provided, the PDF will be saved as 'output.pdf' in the current directory.")
        sys.exit(1)
    
    input_image_paths = sys.argv[1:]
    
    if len(input_image_paths) == 1:
        image_path = input_image_paths[0]
        # Create output path in the same directory as the source image
        file_directory = os.path.dirname(image_path)
        if not file_directory:
            file_directory = "." # Use current directory if no path is specified
        file_basename = os.path.splitext(os.path.basename(image_path))[0]
        output_pdf_path = os.path.join(file_directory, f"{file_basename}.pdf")
    else:
        # For multiple images, save as output.pdf in the current directory
        output_pdf_path = "output.pdf"
        
    convert_images_to_pdf(input_image_paths, output_pdf_path)
