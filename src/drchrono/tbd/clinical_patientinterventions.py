from . import session 

class PATIENTINTERVENTIONS(object):

    def __inti__(self, patient_intervention_id=None):
        self.patient_intervention_id = patient_intervention_id

    @staticmethod
    def patient_interventionlist():
        path = 'https://app.drchrono.com/api/patient_interventions'
        list_response = []
        while path:
            data = session.get(path)
            data_json = data.json()
            list_response.extend(data_json['results'])
            path = data_json['next']
        return list_response

    @classmethod
    def patient_intervention_single(cls, patient_intervention_id):
        path = 'https://app.drchrono.com/api/patient_interventions/{}'.format(patient_intervention_id)
        try: 
            data = session.get(path)
            if data == 200:
                data_json = data.json()
                return data_json
            else:
                print('Error: {}'.format(data))
        except Exception as e:
            print(e)