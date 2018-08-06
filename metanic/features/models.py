from django.utils import text

from metanic.core import models
from metanic.features import managers


class Feature(models.CreateUpdateModel):
    """ Defines a specific feature implemented by Metanic. """

    name = models.CharField(max_length=32)
    identifier = models.SlugField(blank=True, unique=True)

    def save(self, *args, **kwargs):
        if not self.identifier:
            self.identifier = text.slugify(self.name)

        return super(Feature, self).save(*args, **kwargs)

    def __str__(self):
        return self.name


class FeatureValue(models.CreateUpdateModel):
    objects = managers.FeatureValueManager()


class BooleanFeatureValue(FeatureValue):
    value = models.BooleanField()


class StringFeatureValue(FeatureValue):
    value = models.TextField()


class NumericFeatureValue(FeatureValue):
    value = models.DecimalField(max_digits=11, decimal_places=3)


class FeatureUsage(models.MultiSiteModel, models.CreateUpdateModel):
    """ Defines a specific way that a feature is being used. """

    feature = models.ForeignKey(
        'features.Feature',
        related_name='usage',
        db_index=True,
        on_delete=models.CASCADE,
    )

    value = models.ForeignKey(
        'features.FeatureValue',
        related_name='usage',
        db_index=True,
        on_delete=models.CASCADE,
    )

    objects = managers.FeatureUsageManager()
