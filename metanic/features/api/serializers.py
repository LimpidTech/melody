from metanic.rest import serializers

from metanic.features import models


class FeatureValueSerializer(serializers.MetanicModelSerializer):
    class Meta(serializers.MetanicModelSerializer.Meta):
        # TODO: Support polymorphic Model instances as provided
        model = models.FeatureValue

        fields = (
            'url',
            'local_reference',
            'value',
        )


class FeatureSerializer(serializers.MetanicModelSerializer):
    class Meta(serializers.MetanicModelSerializer.Meta):
        model = models.Feature

        fields = (
            'url',
            'local_reference',
            'name',
            'identifier',
        )


class FeatureUsageSerializer(serializers.MetanicModelSerializer):
    feature = FeatureSerializer()

    class Meta(serializers.MetanicModelSerializer.Meta):
        model = models.FeatureUsage

        depth = 1

        fields = (
            'url',
            'local_reference',
            'feature',
        )
