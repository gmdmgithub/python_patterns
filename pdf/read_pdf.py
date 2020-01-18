import pdfplumber #good library to read text (not scanned pdf files)


from PIL import Image
import pytesseract
from pdf2image import convert_from_path, convert_from_bytes

import uuid

def is_text_pdf(file_path):
    with pdfplumber.open(file_path) as pdf:
        return len(pdf.metadata) >0

def read_text_pdf(file_path):
    with pdfplumber.open(file_path) as pdf:
        text = []
        for page in pdf.pages:
            text.append(page.extract_text())
            print(text[-1])

def convert_pdf_to_images(file_path):
    files = []
    images = convert_from_path(pdf_file, dpi=300)
    for i, page in enumerate(images):
        unique_id = str(uuid.uuid1()).replace('-','')
        img_name= f"image_page_{i}_{unique_id}.jpg" 
        page.save(img_name, 'JPEG')
        files.append(img_name)
    return files

def read_scanned_pdf(file_path):
    text = pytesseract.image_to_string(Image.open(file_path),lang='spa') 
    print(text)
    return text

relative_path = './../'
pdf_file = f"{relative_path}scan0025.pdf"
# pdf_file = f"{relative_path}not_scan0000.pdf"

def generate_text(pdf_file):
    if is_text_pdf(pdf_file):
        print('We got pdf with text!!')
        read_text_pdf(pdf_file)
    else:
        print('Digitized pdf is processing ...')
        image_files = convert_pdf_to_images(pdf_file)
        for image_file in image_files:
            read_scanned_pdf(image_file)

def pdf_from_scan(file_name)
    # generate pdf form scan
    pdf = pytesseract.image_to_pdf_or_hocr(, extension='pdf')
    with open('test.pdf', 'w+b') as f:
        f.write(pdf) 

generate_text(pdf_file)