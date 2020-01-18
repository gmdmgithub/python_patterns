import pdfplumber

def read_pdf(file_path):
    with pdfplumber.open(file_path) as pdf:
        print(pdf.metadata)
        for page in pdf.pages:
            print(page.extract_text())
    

# pdf_file = "./../scan0025.pdf"
pdf_file = "./../not_scan0000.pdf"
read_pdf(pdf_file))
