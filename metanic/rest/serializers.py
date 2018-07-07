from rest_framework.serializers import HyperlinkedModelSerializer
from rest_framework.serializers import SerializerMethodField

# Using noqa here to mirror the interface from rest_framework.serializers
from rest_framework.serializers import *  # noqa


class CurrentSiteDefault(object):
    def set_context(self, serializer_field):
        request = serializer_field.context['request']
        self.site = getattr(request, 'site', None)

    def __call__(self):
        return self.site

    def __repr__(self):
        return unicode_to_repr('%s()' % self.__class__.__name__)


class MetanicModelSerializer(HyperlinkedModelSerializer):
    local_reference = SerializerMethodField()

    def get_local_reference(self, instance):
        return getattr(instance, 'pk')