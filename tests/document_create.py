import fpdf
from dotenv import load_dotenv
load_dotenv()
import os
from src.drchrono import drc

drc_client = drc(api_key=os.getenv('DRCHRONO_API_TOKEN'))

# pdf settings
pdf = fpdf.FPDF(format='letter')
pdf.add_page()
pdf.set_font("Arial", size=12)

# Create a fake document dictionary 
f_document = {  'date': '2017-01-01', 
                'description': 'fake document', 
                'note': 'this is a fake document',
                'metatags': 'fake document'}

for key, value in f_document.items():
    pdf.cell(200, 10, txt=key + ': ' + value, ln=1, align='L')

pdf.output("new_test_myfile.pdf")

files = {'document': open('src/new_test_myfile.pdf', 'rb')}

drc_client.documents().create_document(date='2017-01-01', description='testdocumentnov21', doctor=os.getenv('DRCHRONO_DOCTOR_ID'), 
            patient=os.getenv('DRCHRONO_PATIENT_ID'), metatags='["fake-pdf", "document"]',
            document=files)
            






