from rest_framework.authentication import BasicAuthentication 
from rest_framework.authentication import SessionAuthentication

class RestSessionAuthentication(SessionAuthentication):
    def enforce_csrf(self, request):
        """ Override this to not verify CSRF since these APIs don't need it. """

        # TODO: Don't allow SessionAuthentication in production