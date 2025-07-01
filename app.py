import os
import io
from flask import Flask, request, render_template, send_file
from PIL import Image
from werkzeug.utils import secure_filename

app = Flask(__name__)
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024  # 16MB max upload size

@app.route('/', methods=['GET'])
def index():
    """Renders the main page with the file upload form."""
    return render_template('index.html')

@app.route('/convert', methods=['POST'])
def convert():
    """Handles image uploads, converts them to a single PDF, and returns it."""
    if 'images' not in request.files:
        return "No file part in the request", 400

    files = request.files.getlist('images')
    if not files or files[0].filename == '':
        return "No images selected for uploading", 400

    pil_images = []
    for file in files:
        if file and allowed_file(file.filename):
            try:
                image = Image.open(file.stream)
                if image.mode == 'RGBA':
                    image = image.convert('RGB')
                pil_images.append(image)
            except Exception as e:
                print(f"Could not process file {file.filename}: {e}")
                # Optionally, you can return an error to the user
                # return f"Error processing file {file.filename}", 500

    if not pil_images:
        return "No valid images found to convert", 400

    # Save PDF to a memory buffer
    pdf_buffer = io.BytesIO()
    pil_images[0].save(
        pdf_buffer,
        "PDF",
        resolution=100.0,
        save_all=True,
        append_images=pil_images[1:]
    )
    pdf_buffer.seek(0)

    return send_file(
        pdf_buffer,
        as_attachment=True,
        download_name='converted.pdf',
        mimetype='application/pdf'
    )

def allowed_file(filename):
    """Checks if the file extension is allowed."""
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in {'png', 'jpg', 'jpeg', 'gif'}

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=4000, debug=True)
