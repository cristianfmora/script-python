import os
import PyPDF2

def extract_invoice_info(pdf_file_path):

    with open(pdf_file_path, 'rb') as file:
        pdf_reader = PyPDF2.PdfReader(file)
        text = ''

        for page_num in range(len(pdf_reader.pages)):
            page = pdf_reader.pages[page_num]
            text += page.extract_text()
            print(text)

extract_invoice_info("/home/dev/python/ACA")