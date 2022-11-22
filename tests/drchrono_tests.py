from src.drchrono import drc

drc_client = drc()
drc_client = drc(api_key='123')

### Create fake datasets 
f_users, f_doctors, f_patients, f_appointments = drc.faker().generate(20, 40, 150, 500)




drc_client.api_key
drc_client.version
drc_client.version_patients

drc_client.patients().patientlist
# or 
drc(api_key='123').patients().patientlist




