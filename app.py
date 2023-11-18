from flask import Flask, render_template, request
import pytesseract
from PIL import Image

app = Flask(__name__)

# Path to the Tesseract-OCR executable (change this according to your system)
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/extract_text', methods=['POST'])
def extract_text():
    if request.method == 'POST':
        # Get the uploaded image file
        uploaded_file = request.files['file']
        
        # Save the uploaded file
        uploaded_file.save(uploaded_file.filename)
        
        # Perform OCR on the uploaded image
        extracted_text = extract_text_from_image(uploaded_file.filename)
        
        return render_template('result.html', extracted_text=extracted_text)

def extract_text_from_image(image_path):
    image = Image.open(image_path)
    text = pytesseract.image_to_string(image)
    return text

if __name__ == '__main__':
    app.run(debug=True)
