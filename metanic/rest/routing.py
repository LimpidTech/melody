import importlib
import random
import string

from django.conf import settings
from rest_framework import routers

from metanic.rest import routing

API_CLASS_SUFFIXES = ['ViewSet']

INSTALLED_APPS = settings.INSTALLED_APPS


def camel_case_to_snake_case(name):
    if len(name) < 2:
        return name.lower()

    result = name[0].lower()
    upper_characters = set(string.ascii_uppercase)

    for character in name[1:]:
        if character in upper_characters:
            result += '_'

        result += character.lower()

    return result


def import_service_module(app):
    try:
        return importlib.import_module('{}.api.viewsets'.format(app))
    except ImportError:
        return None


def register_viewsets(module):
    for attribute_name in dir(module):
        for suffix in API_CLASS_SUFFIXES:
            if attribute_name.endswith(suffix):
                url_name = attribute_name[:len(attribute_name) - len(suffix)]
                snake_case_url_name = camel_case_to_snake_case(url_name)
                base_name = snake_case_url_name.replace('_', '-').lower()

                if snake_case_url_name.startswith('base_'):
                    continue

                routing.router.register(
                    snake_case_url_name,
                    getattr(module, attribute_name),
                    base_name=base_name,
                )


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


class MetanicRouter(BaseRouter):
    def autodiscover(self):
        for app_name in INSTALLED_APPS:
            register(app_name)


router = MetanicRouter()
