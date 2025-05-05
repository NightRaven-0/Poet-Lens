from flask import Flask, request, jsonify
from flask_cors import CORS
import os
from Utils.image_caption import generate_caption
from Utils.generate_poem import generate_poem

app = Flask(__name__)
CORS(app)

UPLOAD_FOLDER = 'uploads'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

@app.route('/', methods=['GET'])
def home():
    return "Hello, Flask is working!"

@app.route('/upload', methods=['POST'])
def upload_image():
    if 'image' not in request.files:
        return jsonify({'error': 'No image part in request'}), 400

    image = request.files['image']
    if image.filename == '':
        return jsonify({'error': 'No selected file'}), 400

    filepath = os.path.join(UPLOAD_FOLDER, image.filename)
    image.save(filepath)

    caption = generate_caption(filepath)
    poem = generate_poem(caption)
    return jsonify({'message': 'Image uploaded successfully', 
                    'filename': image.filename, 
                    'caption': caption,
                    'poem': poem }), 200

if __name__ == '__main__':
    app.run(debug=True)
