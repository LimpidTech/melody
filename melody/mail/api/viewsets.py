from django import http

from rest_framework import generics
from rest_framework import response
from rest_framework import viewsets

from . import serializers


class MailViewSet(viewsets.ViewSet, generics.GenericAPIView):
    permission_classes = ()
    serializer_class = serializers.MailSerializer

    def create(self, request, action=None):
        serializer = self.serializer_class(data=request.data)

        if not serializer.is_valid():
            raise http.Http404()

        return response.Response(serializer.data)
