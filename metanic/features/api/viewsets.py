from metanic.rest import viewsets

from metanic.features import models
from metanic.features.api import serializers


class FeatureUsageViewSet(viewsets.MetanicModelViewSet):
    serializer_class = serializers.FeatureUsageSerializer

    queryset = models.FeatureUsage.objects             \
                     .with_related_subclasses('value') \
                     .select_related('feature')


class FeatureViewSet(viewsets.MetanicModelViewSet):
    serializer_class = serializers.FeatureUsageSerializer

    queryset = models.Feature.objects                  \
                     .select_related('feature')
