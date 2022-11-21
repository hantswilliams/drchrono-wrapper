from ..utils.httpclient import HttpClient
from .uris import ROOT_PATIENT_API

class PatientManager: 
    """

    A manager objects that provides a full interface to Drchrono Patient API.
    :param API_key: the drChrono API key
    :type API_key: str
    :returns: an `PatientManager` instance
    :raises: `AssertionError` when no API Key is provided
    
    """

    def __init__(self, API_key):
        assert isinstance(API_key, str), 'You must provide a valid API Key'
        self.API_key = API_key
        self.http_client = HttpClient(API_key, ROOT_PATIENT_API)

    def get_patients(self):
        """
        Retrieves all of the patients based on permissions for logged in user.
        :returns: json 
        """

        status, data = self.http_client.get_json(
            ROOT_PATIENT_API,
            params={'appid': self.API_key},
            headers={'Content-Type': 'application/json'})
            
        return {'status': status, 'data': data}

