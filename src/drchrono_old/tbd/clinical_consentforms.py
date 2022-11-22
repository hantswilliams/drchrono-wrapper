from . import session

class CONSENT(object):

    def __init__(self, consentform_id=None):
        self.consentform_id = consentform_id

    @staticmethod
    def consentformlist():
        path = 'https://app.drchrono.com/api/consent_forms'
        list_response = []
        while path:
            data = session.get(path)
            data_json = data.json()
            list_response.extend(data_json['results'])
            path = data_json['next']
        return list_response

    @classmethod
    def consentform_single(cls, consentform_id):
        path = 'https://app.drchrono.com/api/consent_forms/{}'.format(consentform_id)
        try: 
            data = session.get(path)
            if data == 200:
                data_json = data.json()
                return data_json
            else:
                print('Error: {}'.format(data))
        except Exception as e:
            print(e)