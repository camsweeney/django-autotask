from djautotask import models
from django.conf import settings
import atws


# Might have to move to utils
class DjautotaskSettings:

    def get_settings(self):
        request_settings = {}

        if hasattr(settings, 'DJAUTOTASK_CONF_CALLABLE'):
            request_settings.update(settings.DJAUTOTASK_CONF_CALLABLE())

        return request_settings


class Synchronizer:

    def __init__(self, full=False, *args, **kwargs):
        request_settings = DjautotaskSettings().get_settings()
        self.full = full


class AccountSynchronizer(Synchronizer):
    pass


class ProjectSynchronizer(Synchronizer):
    pass


class TicketSynchronizer(Synchronizer):
    pass


class TicketCategorySynchronizer(Synchronizer):
    pass


class TimeEntrySynchronizer(Synchronizer):
    pass


class TicketSecondaryResourceSynchronizer(Synchronizer):
    pass


class ResourceSynchronizer(Synchronizer):
    pass


class DepartmentSynchronizer(Synchronizer):
    pass


class RoleSynchronizer(Synchronizer):
    pass


class OpportunitySynchronizer(Synchronizer):
    pass
