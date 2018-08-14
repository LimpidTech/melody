from metanic.rest import viewsets

from metanic.features import models
from metanic.features.api import serializers


class FeatureViewSet(viewsets.MetanicModelViewSet):
    serializer_class = serializers.FeatureSerializer
    queryset = models.Feature.objects


class FeatureValueViewSet(viewsets.MetanicModelViewSet):
    serializer_class = serializers.FeatureValueSerializer

    def get_queryset(self):
        return models.FeatureValue.objects.provided_by(
            site=self.request.site,
            user=self.request.user,
        )


class FeatureUsageViewSet(viewsets.MetanicModelViewSet):
    serializer_class = serializers.FeatureUsageSerializer

    def get_queryset(self):
        return models.FeatureUsage.objects.provided_by(
            site=self.request.site,
            user=self.request.user,
        )
