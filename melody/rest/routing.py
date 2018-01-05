import random
import importlib

from django.conf import settings
from rest_framework import routers

from melody.rest import routing

API_CLASS_SUFFIXES = ['ViewSet']

INSTALLED_APPS = settings.INSTALLED_APPS


def import_service_module(app):
    try:
        return importlib.import_module('{}.api.viewsets'.format(app))
    except ImportError:
        return None


def register_viewsets(module):
    for attribute_name in dir(module):
        for suffix in API_CLASS_SUFFIXES:
            if attribute_name.endswith(suffix):
                url_name = attribute_name.lower()[:len(attribute_name) - len(suffix)]

                view = getattr(module, attribute_name)

                try:
                    routing.router.register(
                        url_name,
                        view,
                        base_name=url_name,
                    )

                except:
                    __import__('pdb').set_trace()


def register(app_name):
    module = import_service_module(app_name)

    if not module:
        return

    register_viewsets(module)


# TODO: Maybe this should just be a setting instead
if settings.DEBUG is True:
    BaseRouter = routers.DefaultRouter
else:
    BaseRouter = routers.SimpleRouter


class MelodyRouter(BaseRouter):
    def autodiscover(self):
        for app_name in INSTALLED_APPS:
            register(app_name)


router = MelodyRouter()
