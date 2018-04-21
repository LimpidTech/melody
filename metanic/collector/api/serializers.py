import importlib
from rest_framework import serializers

from django.conf import settings

COLLECTION_SERIALIZER_TYPES = settings.COLLECTION_SERIALIZER_TYPES

def get_serializer(module_name, attribute_name):
    return getattr(importlib.import_module(module_name), attribute_name)


class MultiResourceRelatedField(serializers.RelatedField):
    def to_representation(self, obj):
        serializer_data = COLLECTION_SERIALIZER_TYPES.get(obj._meta.model_name)

        if serializer_data is None:
            raise ValueError('{} must be in COLLECTION_SERIALIZER_TYPES'.format(
                obj._meta.model_name,
            ))

        Serializer = get_serializer(*serializer_data)

        if Serializer is None:
            raise ValueError('No serializer exists at {}.{}'.format(
                *serializer_data,
            ))

        return Serializer(
            obj,
            context=self.context,
        ).data


class CollectionSerializer(serializers.Serializer):
    url = serializers.HyperlinkedIdentityField(view_name='collection-detail')
    name = serializers.CharField()
    items = MultiResourceRelatedField(many=True, read_only=True)

    def get_items(self, obj):
        return obj.items()
