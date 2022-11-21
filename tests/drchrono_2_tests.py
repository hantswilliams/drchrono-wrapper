from src.drchrono2 import drc


drc_client = drc(api_key='123')

drc_client.api_key


drc_client.patient_manager().get_patients()