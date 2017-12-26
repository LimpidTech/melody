import importlib

from rest_framework import routers
from django.conf import settings


class MelodyRouter(routers.DefaultRouter):
    def autodiscover(self, api_module='api'):
        for installed_app in settings.INSTALLED_APPS:
            try:
                importlib.import_module(f'{installed_app}.{api_module}')
            except ImportError:
                continue


router = MelodyRouter()
