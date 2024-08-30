from flask import Flask, request, jsonify
from paddleocr import PaddleOCR

app = Flask(__name__)

class OCRProcessor:
    def __init__(self, use_angle_cls=True, lang='en', use_space_char=True, show_log=False, enable_mkldnn=True, use_gpu=False):
        self.ocr = PaddleOCR(use_angle_cls=use_angle_cls, lang=lang, use_space_char=use_space_char, show_log=show_log, enable_mkldnn=enable_mkldnn, use_gpu=None)

    def process_image(self, img_path):
        result = self.ocr.ocr(img_path, cls=True)
        ocr_string = ""
        for i in range(len(result[0])):
            ocr_string = ocr_string + result[0][i][1][0] + " "
        return ocr_string

ocr_processor = OCRProcessor()

@app.route('/upload', methods=['POST'])
def upload_image():
    if 'image' not in request.files:
        return jsonify({'error': 'No image provided'}), 400

    image_file = request.files['image']
    if image_file.filename == '':
        return jsonify({'error': 'No selected image'}), 400

    # Save the uploaded image to a temporary location
    image_path = 'temp_image.jpg'
    image_file.save(image_path)

    # Process the uploaded image
    ocr_text = ocr_processor.process_image(image_path)

    # Return the OCR result
    return jsonify({'text': ocr_text})

if __name__ == '__main__':
    app.run(debug=True)
