from pdf2image import convert_from_path
import pytesseract
import utility

from parser_prescription import Prescriptionparser

from parser_patient_details import Patientdetailparser

POPPELER_PATH = r'C:\Release-24.02.0-0\poppler-24.02.0\Library\bin'
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

from PIL import Image

def extract(file_path,file_format):

    #extracting text from pdf file
    pages = convert_from_path(file_path, poppler_path = POPPELER_PATH)
    document_text = ''
    if len(pages)>0:
        page = pages[0]
        processed_image = utility.preprocess_image(page)
        text = pytesseract.image_to_string(processed_image, lang='eng')
        document_text = '\n' + text

    #extract fields from text
    if file_format=='prescription':
         extracted_data = Prescriptionparser(document_text).parse()  # extract data from precription
    elif file_format=='patient_details':
        extracted_data = Patientdetailparser(document_text).parse()
    else:
        raise Exception(f"Inavalid document format: {file_format}")

    return extracted_data

if __name__ == '__main__':
    data = extract('../resources/patient_details/pd_2.pdf','patient_details')
    print(data)