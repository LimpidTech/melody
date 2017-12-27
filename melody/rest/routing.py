import random
import importlib

from rest_framework import routers
from django.conf import settings

from melody.rest import routing


API_CLASS_SUFFIXES = ['ViewSet']

INSTALLED_APPS = settings.INSTALLED_APPS


def import_service_module(app):
    try:
        return importlib.import_module(f'{app}.api.viewsets')
    except ImportError:
        return None


def register_viewsets(module):
    for attribute_name in dir(module):
        for suffix in API_CLASS_SUFFIXES:
            if attribute_name.endswith(suffix):
                url_name = attribute_name.lower()[:len(attribute_name)-len(suffix)]
                routing.router.register(url_name, getattr(module, attribute_name))


def register(app_name):
    module = import_service_module(app_name)
    if module:
        register_viewsets(module)


class MelodyRouter(routers.DefaultRouter):
    def autodiscover(self):
        for app_name in INSTALLED_APPS:
            register(app_name)


router = MelodyRouter()
