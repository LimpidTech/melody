from rest_framework import serializers

from rest_framework.viewsets import ModelViewSet

# We are using noqa here so that we can mirror the interface
# from rest_framwork's viewsets.
from rest_framework.viewsets import *  # noqa

class MetanicModelViewSet(ModelViewSet):
    pass