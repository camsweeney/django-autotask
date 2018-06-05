from djautotask import models
from django.conf import settings


# Might have to move to utils
class DjautotaskSettings:

    def get_settings(self):
        request_settings = {}

        if hasattr(settings, 'DJAUTOTASK_CONF_CALLABLE'):
            request_settings.update(settings.DJAUTOTASK_CONF_CALLABLE())

        return request_settings


class Synchronizer:

    def __init__(self):
        pass
