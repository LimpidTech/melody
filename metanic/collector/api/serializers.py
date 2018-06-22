import importlib
from rest_framework import serializers

from django.conf import settings

DEFAULT_COLLECTION_NAME_FIELD = 'name'
COLLECTION_SERIALIZER_TYPES = settings.COLLECTION_SERIALIZER_TYPES


def get_serializer(module_name, attribute_name):
    return getattr(importlib.import_module(module_name), attribute_name)


def get_serializer_data(context, collection_item):
    serializer_data = COLLECTION_SERIALIZER_TYPES.get(
        collection_item._meta.model_name
    )

    if serializer_data is None:
        raise ValueError('{} must be in COLLECTION_SERIALIZER_TYPES'.format(
            collection_item._meta.model_name,
        ))

    Serializer = get_serializer(*serializer_data)

    if Serializer is None:
        raise ValueError('No serializer exists at {}.{}'.format(
            *serializer_data,
        ))

    return Serializer(collection_item, context=context).data


class CollectionSerializer(serializers.Serializer):
    url = serializers.HyperlinkedIdentityField(view_name='collection-detail')
    name = serializers.SerializerMethodField()

    items = serializers.SerializerMethodField()

    def get_items(self, collection):
        return list(map(
            get_serializer_data,
            [self.context],
            collection.items(self.context['request']),
        ))

    def get_name(self, collection_item):
        collection_name_field = getattr(
            collection_item,
            'collection_name_field',
            DEFAULT_COLLECTION_NAME_FIELD,
        )

        collection_name = getattr(
            collection_item,
            collection_name_field,
            None
        )

        if collection_name is None:
            collection_name = str(collection_item)

        return collection_name
