from . import session

class DOCUMENTS(object):

    def __init__(self, document_id=None):
        self.document_id = document_id

    @staticmethod
    def documentlist():
        path = 'https://app.drchrono.com/api/documents'
        list_response = []
        while path:
            data = session.get(path)
            data_json = data.json()
            list_response.extend(data_json['results'])
            path = data_json['next']
        return list_response

    @classmethod
    def document_single(cls, document_id):
        path = 'https://app.drchrono.com/api/documents/{}'.format(document_id)
        try: 
            data = session.get(path)
            if data == 200:
                data_json = data.json()
                return data_json
            else:
                print('Error: {}'.format(data))
        except Exception as e:
            print(e)