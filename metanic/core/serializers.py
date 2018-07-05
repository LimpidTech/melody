from rest_framework.serializers import *


class CurrentSiteDefault(object):
    def set_context(self, serializer_field):
        request = serializer_field.context['request']
        self.site = getattr(request, 'site', None)

    def __call__(self):
        return self.site

    def __repr__(self):
        return unicode_to_repr('%s()' % self.__class__.__name__)