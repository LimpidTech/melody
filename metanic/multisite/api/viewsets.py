from rest_framework import viewsets
from django.contrib.sites import models

from metanic.multisite.api import serializers


class SiteViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = models.Site.objects.all()
    serializer_class = serializers.SiteSerializer

    def get_queryset(self):
        return self.queryset.filter(domain=self.request.META.get('HTTP_HOST'))