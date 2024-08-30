from flask import Flask, request, jsonify, render_template
from ocrclass import extract_text_from_image

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/api/extract_text", methods=["POST"])
def api_extract_text():
        if "image" not in request.files:
            return "No image uploaded", 400

        image_file = request.files["image"]
        extracted_text = extract_text_from_image(image_file)
        return jsonify({"extracted_text": extracted_text})

if __name__ == "__main__":
    app.run(debug=True)
