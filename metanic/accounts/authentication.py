from django.contrib.auth import authenticate
from django.contrib.auth import login
from rest_framework import authentication


class CSRFExemptAuthentication(authentication.SessionAuthentication):
    def enforce_csrf(self, request):
        """ Override enforce_csrf to not do anything. """


def authenticate_and_login(request, username, password):
    user = authenticate(username=username, password=password)

    if user is not None:
        login(request, user)

    return user