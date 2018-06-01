import inspect
import importlib

from django.conf import settings
from zope.interface import adapter

from . import collection


registry = adapter.AdapterRegistry()


def register(Kind):
    registry.register([], collection.ICollection, Kind.name, Kind())


def all():
    return registry.lookupAll([], collection.ICollection)


def lookup(name):
    return registry.lookup([], collection.ICollection, name)


def register_attributes(module):
    for attribute_name in dir(module):
        item = getattr(module, attribute_name)

        if not inspect.isclass(item):
            continue

        if collection.ICollection.implementedBy(item):
            register(item)

def append_module_name(module_name):
    return '{}.{}'.format(module_name, 'collections')

def import_module(module_name):
    try:
        return importlib.import_module(module_name)
    except ImportError:
        return

def autodiscover():
    module_names = map(append_module_name, settings.INSTALLED_APPS)
    modules = filter(None, map(import_module, module_names))
    return list(map(register_attributes, modules))
