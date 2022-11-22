from . import session 

class CAREPLANS(object):

    def __init__(self, careplan_id=None):
        self.careplan_id = careplan_id

    @staticmethod
    def careplanlist():
        path = 'https://app.drchrono.com/api/care_plans'
        list_response = []
        while path:
            data = session.get(path)
            data_json = data.json()
            list_response.extend(data_json['results'])
            path = data_json['next']
        return list_response

    @classmethod
    def careplan_single(cls, careplan_id):
        path = 'https://app.drchrono.com/api/care_plans/{}'.format(careplan_id)
        try: 
            data = session.get(path)
            if data == 200:
                data_json = data.json()
                return data_json
            else:
                print('Error: {}'.format(data))
        except Exception as e:
            print(e)