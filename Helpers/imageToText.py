from PIL import Image
from pytesseract import pytesseract

pytesseract.tesseract_cmd = r"c:\Program Files\Tesseract-OCR\tesseract.exe"

def toText(image):
    a=pytesseract.image_to_string(Image.open(image), lang="tur")
    return a

# print(toText('uyari.png'))