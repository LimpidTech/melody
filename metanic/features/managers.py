from django.db import connection
from django.db import models

from model_utils import managers


class FeatureValueManager(managers.InheritanceManager):
    pass


class FeatureUsageManager(models.Manager):
    def with_related_subclasses(self, field_name):
        fields = self.model._meta._forward_fields_map
        FeatureValue = fields[field_name].related_model

        return self.prefetch_related(
            models.Prefetch(
                lookup=field_name,
                queryset=FeatureValue.objects.select_subclasses(),
            )
        )

    def provided_by(self, *, site, user):
        # TODO: Take the user into account for user-specific overrides, A/B/*
        # testing, etc.

        result = self                           \
            .with_related_subclasses('value') \
            .select_related('feature')        \
            .filter(sites=site)

        return result
