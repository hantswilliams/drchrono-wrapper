from . import session 

class PATIENTMESSAGES(object):

    def __init__(self, patient_message_id=None):
        self.patient_message_id = patient_message_id

    @staticmethod
    def patient_messagelist():
        path = 'https://app.drchrono.com/api/patient_messages'
        list_response = []
        while path:
            data = session.get(path)
            data_json = data.json()
            list_response.extend(data_json['results'])
            path = data_json['next']
        return list_response

    @classmethod
    def patient_message_single(cls, patient_message_id):
        path = 'https://app.drchrono.com/api/patient_messages/{}'.format(patient_message_id)
        try: 
            data = session.get(path)
            if data == 200:
                data_json = data.json()
                return data_json
            else:
                print('Error: {}'.format(data))
        except Exception as e:
            print(e)