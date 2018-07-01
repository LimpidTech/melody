from django.contrib.sites import models

from rest_framework import serializers


class SiteSerializer(serializers.HyperlinkedModelSerializer):
    class Meta(object):
        depth = 1
        model = models.Site

        fields = (
            'domain',
        )