from django import http

from rest_framework import response
from rest_framework import viewsets

from metanic.collector import registration

from . import serializers


class CollectionViewSet(viewsets.ViewSet):
    authentication_classes = ()
    permission_classes = ()

    serializer_class = serializers.CollectionSerializer

    def list(self, request):
        return response.Response([], status=200)

    def retrieve(self, request, pk=None):
        if pk is None:
            raise http.HttpResponseBadRequest(
                'A collection name is required.',
            )

        instance = registration.lookup(pk)

        if instance is None:
            raise http.Http404(
                'No collections were found matching the given name.',
            )

        serializer = self.serializer_class(
            instance(self.request),
            many=True,
            context={
                'request': self.request,
            }
        )

        return response.Response(serializer.data, status=200)
