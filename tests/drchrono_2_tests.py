from src.drchrono2 import drc

drc_client = drc(api_key='123')

drc_client.api_key
pt_manager = drc_client.patient_manager()
pt_manager.get_all()


