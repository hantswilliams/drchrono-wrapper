from src.drchrono import drc
import fpdf
import os
from dotenv import load_dotenv

load_dotenv()

# drc_client = drc()
drc_client = drc(api_key=os.getenv('DRCHRONO_API_TOKEN'))


drc_client.api_key
drc_client.api_key
drc_client.version
drc_client.version_patients

###############################################
###############################################
###############################################

### Create fake datasets 
f_users, f_doctors, f_patients, f_appointments = drc.faker().generate(20, 40, 150, 500)


### Retrieve datasets
patient_all = drc_client.patients().patientlist
patient_single = drc_client.patients().patient_single(patient_id='104612001')
doctor_list = drc_client.doctors().doctorlist
appointments = drc_client.appointments().appointment_list(appointment_startdate='2019-01-01')

#### fake doc create 
#### fake doc create 
#### fake doc create 
#### fake doc create 
#### fake doc create 
#### fake doc create 
#### fake doc create 

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

drc_client.documents().create_document(date='2017-01-01', description='testdocumentnov21_ANOTHER ONE', doctor=os.getenv('DRCHRONO_DOCTOR_ID'), 
            patient=os.getenv('DRCHRONO_PATIENT_ID'), metatags='["fake-pdf", "document"]',
            document=files)

#######################
#######################
#######################
#######################
#######################
#######################
#######################
#######################







