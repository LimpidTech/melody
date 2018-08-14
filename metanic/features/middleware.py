# We import this because references to class names should be easily refactored.
# Referencing names by variable instead of rewriting a string everwhere
# enforces this guideline.
from metanic.core.middleware import sites
from metanic.features import models


def get_feature_usage(usages):
    features = {}

    for usage in usages:
        value = usage.value.value

        if value:
            features[usage.feature.identifier] = value

    return features


class SiteFeaturesMiddleware(object):
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if not hasattr(request, 'site'):
            raise EnvironmentError(
                (
                    'Configuration must provide {}'
                    'before {} in the MIDDLEWARE setting.'
                ).format(
                    self.__class__.__name__,
                    sites.MultiSiteMiddleware.__name__,
                )
            )

        # Assign request.features before we continue processing the response.
        request.features = get_feature_usage(
            models.FeatureUsage.objects.provided_by(
                site=request.site,
                user=request.user,
            )
        )

        return self.get_response(request)
