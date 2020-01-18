from PIL import Image
import pytesseract
from pdf2image import convert_from_path, convert_from_bytes


def ocr_core(filename):
    """
    This function will handle the core OCR processing of images.
    """
    text = pytesseract.image_to_string(Image.open(filename)) 
    return text


# print(ocr_core('./../image_0.jpg'))

# convert pdf to image
relative_path = './../'
pdf_file = f"{relative_path}scan0025.pdf"
images = convert_from_path(pdf_file, dpi=500)

for i, page in enumerate(images):
    img_name= f"image_{i}.jpg" 
    page.save(img_name, 'JPEG')
    print(ocr_core(f'{relative_path}{img_name}'))

