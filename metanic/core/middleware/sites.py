from django.core.cache import cache
from django.contrib.sites import models


class MultiSiteMiddleware(object):
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # NOTE: Trade-off here is that using HTTP_HOST means that
        #       services must be in front of a proxy which enusres
        #       accuracy of the HOST header for security reasons. If
        #       not, then attackers can send requests with fake hosts.

        # TODO: Cache a site <--> ID mapping for performance reasons.

        # NOTE: The cache needs to watch for signals on model changes so that
        #       it gets invalidated when necessary.

        hostname = request.META['HTTP_HOST']
    
        # NOTE: This should probably be optional, since it could allow
        #       for some dangerous DDoS action if the previous comment(s)
        #       were to be ignored.
        site, _ = models.Site.objects.get_or_create(domain=hostname)

        request.site = site
        response = self.get_response(request)

        return response