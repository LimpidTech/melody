from django import http

from rest_framework import response
from rest_framework import generics
from rest_framework import viewsets

from metanic.collector import collection
from metanic.collector import registration

from . import serializers


class CollectionViewSet(viewsets.ViewSet):
    permission_classes = ()
    serializer_class = serializers.CollectionSerializer

    def list(self, request):
        return response.Response([], status=200)

    def retrieve(self, request, pk=None):
        if pk is None:
            raise http.HttpResponseBadRequest(
                'A collection name is required.',
            )

        Kind = registration.lookup(pk)

        if Kind is None:
            raise http.Http404(
                'No collections were found matching the given name.',
            )

        instance = Kind(self.request)

        serializer = self.serializer_class(
            instance, context={
                'request': self.request,
            }
        )

        return response.Response(serializer.data, status=200)
