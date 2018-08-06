from metanic.rest import serializers

from metanic.features import models


class FeatureUsageSerializer(serializers.MetanicModelSerializer):
    class Meta(serializers.MetanicModelSerializer.Meta):
        model = models.FeatureUsage
        fields = (
            'url',
            'name',
            'slug',
        )


class FeatureUsageSerializer(serializers.MetanicModelSerializer):
    class Meta(serializers.MetanicModelSerializer.Meta):
        model = models.FeatureUsage
        fields = ('url',)
