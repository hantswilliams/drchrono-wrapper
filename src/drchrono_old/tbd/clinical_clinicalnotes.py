from . import session 

class CLINICALNOTES(object):

    def __init__(self, clinical_note_id=None):
        self.clinical_note_id = clinical_note_id

    @staticmethod
    def clinicalnotelist():
        path = 'https://app.drchrono.com/api/clinical_notes'
        list_response = []
        while path:
            data = session.get(path)
            data_json = data.json()
            # check if results exist in data_json
            if 'results' in data_json:
                list_response.extend(data_json['results'])
                path = data_json['next']
            else:
                print('Error: {}'.format(data))
                break
                path = None
        return list_response

    @classmethod
    def clinicalnote_single(cls, clinical_note_id):
        path = 'https://app.drchrono.com/api/clinical_notes/{}'.format(clinical_note_id)
        try: 
            data = session.get(path)
            if data == 200:
                data_json = data.json()
                return data_json
            else:
                print('Error: {}'.format(data))
        except Exception as e:
            print(e)
            