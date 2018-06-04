import inspect
import importlib

from django.conf import settings
from zope.interface import adapter

from . import collection


registry = adapter.AdapterRegistry()


def register(Kind):
    """ Register a given Collection type with the collector. """

    registry.register(
        [],
        collection.ICollection,
        Kind.name,
        Kind()
    )


def all():
    return registry.lookupAll([], collection.ICollection)


def lookup(name):
    return registry.lookup([], collection.ICollection, name)


def is_valid_collector(item):
    return inspect.isclass(item) and collection.ICollection.implementedBy(item)

def register_attributes(module):
    for attribute_name in dir(module):
        item = getattr(module, attribute_name)

        if is_valid_collector(item):
            register(item)


def append_module_name(module_name):
    return module_name + '.collections'


def import_module(module_name):
    try:
        return importlib.import_module(module_name)
    except ImportError:
        return


def autodiscover():
    module_names = map(append_module_name, settings.INSTALLED_APPS)
    modules = filter(None, map(import_module, module_names))
    return list(map(register_attributes, modules))
