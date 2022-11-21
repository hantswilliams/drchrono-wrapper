
from .constants import *
from .patients import patient_manager

class drc:

    """
    Entry point class providing ad-hoc API clients for each drChrono API.

    :param api_key: the OWM API key
    :type api_key: str
    :param version: the OWM API version

    """

    def __init__(self, api_key, config=None):
        assert api_key is not None, 'API Key must be set'
        self.api_key = api_key


    @property
    def version(self):
        """
        Returns the current version of the Drchrono API wrapper library
        :returns: `tuple`
        """
        return constants.DRC_VERSION

    def patient_manager(self):
        """
        Gives a `pyowm.agro10.agro_manager.AgroManager` instance that can be used to read/write data from the
        Agricultural API.
        :return: a `pyowm.agro10.agro_manager.AgroManager` instance
        """
        return patient_manager.PatientManager(self.api_key)
