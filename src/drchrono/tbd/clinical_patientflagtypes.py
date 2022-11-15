from . import session 

class PATIENTFLAGTYPES(object):

    def __init__(self, patient_flag_type_id=None):
        self.patient_flag_type_id = patient_flag_type_id

    @staticmethod
    def patientflagtypelist():
        path = 'https://app.drchrono.com/api/patient_flag_types'
        list_response = []
        while path:
            data = session.get(path)
            data_json = data.json()
            list_response.extend(data_json['results'])
            path = data_json['next']
        return list_response

    @classmethod
    def patientflagtype_single(cls, patient_flag_type_id):
        path = 'https://app.drchrono.com/api/patient_flag_types/{}'.format(patient_flag_type_id)
        try: 
            data = session.get(path)
            if data == 200:
                data_json = data.json()
                return data_json
            else:
                print('Error: {}'.format(data))
        except Exception as e:
            print(e)