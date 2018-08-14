from django.contrib.sites import models

from metanic.rest import serializers


class SiteSerializer(serializers.MetanicModelSerializer):
    class Meta(serializers.MetanicModelSerializer.Meta):
        depth = 1
        model = models.Site

        fields = (
            'url',
            'local_reference',
            'name',
            'domain',
        )
