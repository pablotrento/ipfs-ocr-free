import pytesseract
from PIL import Image

# Path to the Tesseract-OCR executable (change this according to your system)
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

def extract_text_from_image(image_path):
    # Open the image using PIL (Python Imaging Library)
    image = Image.open(image_path)
    
    # Use pytesseract to do OCR on the image
    text = pytesseract.image_to_string(image)
    
    return text

# Replace 'image_path' with the path to your image file
image_text = extract_text_from_image(r'.\photo.jpg')
print(image_text)
