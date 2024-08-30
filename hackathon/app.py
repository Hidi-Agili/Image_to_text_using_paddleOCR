from flask import Flask, request, jsonify, render_template
from ocr import ocr_processor
import os

app = Flask(__name__)

@app.route("/index", methods=["GET"])
def index():
    return render_template("index.html")

@app.route("/upload", methods=["POST"])
def upload_image():
        if "image" not in request.files:
            return jsonify({'error': "No image uploaded"}), 400

        image_file = request.files["image"]
        if image_file.filename == '':
            return jsonify({'error': 'No selected image'}), 400
        
        #save the uploaded image to a temporary location
        image_path = 'temp_image.jpg'
        image_file.save(image_path)

        try:
            # Process the uploaded image
            ocr_text = ocr_processor.process_image(image_path)
        finally:
            # Remove the temporary file
            if os.path.exists(image_path):
                os.remove(image_path)

        # Return the OCR result
        return jsonify({'text': ocr_text})

if __name__ == "__main__":
    app.run(debug=True)
