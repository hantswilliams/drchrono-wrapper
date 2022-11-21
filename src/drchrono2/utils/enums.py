from .databoxes import SubscriptionType


class SubscriptionTypeEnum:
    """
    Allowed OpenWeatherMap subscription types
    """
    FREE = SubscriptionType('free', 'api', False)
    STARTUP = SubscriptionType('startup', 'api', True)
    DEVELOPER = SubscriptionType('developer', 'api', True)
    PROFESSIONAL = SubscriptionType('professional', 'api', True)
    ENTERPRISE = SubscriptionType('enterprise', 'api', True)

    @classmethod
    def lookup_by_name(cls, name):
        for i in SubscriptionTypeEnum.items():
            if i.name == name:
                return i
        raise ValueError('Subscription type not allowed')

    @classmethod
    def items(cls):
        """
        All values for this enum
        :return: list of `pyowm.commons.enums.SubscriptionType`
        """
        return [
            cls.FREE,
            cls.STARTUP,
            cls.DEVELOPER,
            cls.PROFESSIONAL,
            cls.ENTERPRISE
        ]

    def __repr__(self):
        return "<%s.%s>" % (__name__, self.__class__.__name__)


