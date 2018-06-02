from zope.interface import Interface
from zope.interface import Attribute


class ICollection(Interface):
    """ Provides an interface for getting named lists of resources. """

    name = Attribute(""" A friendly name for this collection """)

    def __call__(request):
        """ Create a new Collection for the given request. """

    def items(request):
        """ Gets a list of resources in this collection. """


class Collection(object):
    """ Implements boilerplate behaviors for Collection objects. """

    def __init__(self):
        self.resource_url = self.name.lower()

    def __call__(self, request):
        return self.items(request)
