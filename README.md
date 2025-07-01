# Image to PDF Converter

This project contains a Python script to convert one or more image files (e.g., PNG, JPG) into a single PDF file.

## Setup

1.  **Install dependencies:**
    Open your terminal and run the following command in the project directory to install the required `Pillow` library:
    ```bash
    pip install -r requirements.txt
    ```

## Usage

Run the script from your terminal, providing the paths to the image(s) you want to convert as arguments.

### Convert a single image

Provide one image path. The output PDF will be saved in the same directory with the same base name.

```bash
python image_to_pdf.py /path/to/your/image.jpg
```

### Convert multiple images

Provide multiple image paths. The images will be combined into a single PDF named `output.pdf` in your current directory.

```bash
python image_to_pdf.py /path/to/image1.png /path/to/image2.jpg
```
