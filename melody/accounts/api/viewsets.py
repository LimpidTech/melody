from django.contrib.auth import logout
from django.contrib.auth import models as auth_models
from melody.accounts import authentication
from rest_framework import generics
from rest_framework import response
from rest_framework import viewsets

from . import serializers


class UserViewSet(viewsets.ModelViewSet):
    queryset = auth_models.User.objects.all()
    serializer_class = serializers.UserSerializer

    def filter_queryset(self, queryset):
        return queryset.filter(pk=self.request.user.pk)


class AuthenticationViewSet(viewsets.ViewSet, generics.GenericAPIView):
    permission_classes = ()
    serializer_class = serializers.AuthenticationSerializer

    def create(self, request):
        logout(request)
        input_serializer = self.get_serializer(data=request.data)

        if not input_serializer.is_valid():
            return response.Response({
                'meta': {'error': True},
                'result': serializer.errors
            }, status=400)

        user = authentication.authenticate_and_login(
            request,
            input_serializer.data['username'],
            input_serializer.data['password'],
        )

        if user is None:
            return response.Response(None, status=400)

        return response.Response(None, status=200)
