from . import session

class PATIENTCOMMUNICATIONS(object):

    def __init__(self, patient_comm_id=None):
        self.patient_comm_id = patient_comm_id

    @staticmethod
    def patient_commlist():
        path = 'https://app.drchrono.com/api/patient_communications'
        list_response = []
        while path:
            data = session.get(path)
            data_json = data.json()
            list_response.extend(data_json['results'])
            path = data_json['next']
        return list_response

    @classmethod
    def patient_comm_single(cls, patient_comm_id):
        path = 'https://app.drchrono.com/api/patient_communications/{}'.format(patient_comm_id)
        try: 
            data = session.get(path)
            if data == 200:
                data_json = data.json()
                return data_json
            else:
                print('Error: {}'.format(data))
        except Exception as e:
            print(e)