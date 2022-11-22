from .. import session

class TELEHEALTH(object):

    """

    https://app.drchrono.com/api-docs/#tag/Clinical/operation/telehealth_appointments_list
    
    {
    "data": [
        {
        "appointment": 0,
        "created_at": "string",
        "duration": 0,
        "overlapping_duration": "string",
        "sent_patient_email": null,
        "telehealth_url": "string",
        "updated_at": "string"
        }
    ],
    "next": "string",
    "previous": "string"
    }
    
    """

    def __init__(self, telehealthappointment_startdate=None, telehealthappointment_enddate=None, telehealthappointment_id=None):
        self.telehealthappointment_startdate = telehealthappointment_startdate
        self.telehealthappointment_enddate = telehealthappointment_enddate
        self.telehealthappointment_id = telehealthappointment_id

    @staticmethod
    def telehealth_list_types():
        dictionaryResponse = {
            "data": [
                {
                "appointment": 0,
                "created_at": "string",
                "duration": 0,
                "overlapping_duration": "string",
                "sent_patient_email": "null",
                "telehealth_url": "string",
                "updated_at": "string"
                }
            ],
            "next": "string",
            "previous": "string"
        }
        return dictionaryResponse

    @staticmethod
    def telehealth_list():
        path = 'https://drchrono.com/api/telehealth_appointments'
        list_response = []
        while path:
            data = session.get(path).json()
            list_response.extend(data['results'])
            path = data['next'] # A JSON null on the last page
        return list_response

    @classmethod
    def telehealth_single(cls, telehealthappointment_id):
        path = 'https://drchrono.com/api/telehealth_appointments/{}'.format(telehealthappointment_id)
        try: 
            data = session.get(path)
            if data == 200:
                data_json = data.json()
                return data_json
            else:
                print('Error: {}'.format(data))
        except Exception as e:
            print(e)

