from django.contrib.auth import logout
from django.contrib.auth import models as auth_models
from django.utils import decorators
from django.views.decorators import csrf
from rest_framework import authentication as rest_authentication
from rest_framework import generics
from rest_framework import response
from rest_framework import throttling
from rest_framework import viewsets
from rest_framework_jwt import authentication as jwt_authentication

from melody.accounts import authentication

from . import serializers

ensure_csrf = decorators.method_decorator(csrf.ensure_csrf_cookie)


class UserViewSet(viewsets.ModelViewSet):
    queryset = auth_models.User.objects.all()
    serializer_class = serializers.UserSerializer

    def filter_queryset(self, queryset):
        """ Ensure that users can not view details for other users. """

        if self.request.user.is_superuser:
            return queryset

        return queryset.filter(pk=self.request.user.pk)


class AuthenticationViewSet(viewsets.ViewSet, generics.GenericAPIView):
    permission_classes = ()
    serializer_class = serializers.AuthenticationSerializer

    throttle_classes = (
        throttling.AnonRateThrottle,
        throttling.UserRateThrottle,
    )

    authentication_classes = (
        authentication.CSRFExemptAuthentication,
        jwt_authentication.JSONWebTokenAuthentication,
        rest_authentication.TokenAuthentication,
    )

    @ensure_csrf
    def create(self, request):
        logout(request)
        input_serializer = self.get_serializer(data=request.data)

        if not input_serializer.is_valid():
            return response.Response(
                {
                    'meta': {
                        'error': True
                    },
                    'result': input_serializer.errors
                },
                status=400
            )

        user = authentication.authenticate_and_login(
            request,
            input_serializer.data['username'],
            input_serializer.data['password'],
        )

        if user is None:
            return response.Response({}, status=400)

        return response.Response({}, status=200)

    @ensure_csrf
    def destroy(self, request, pk=None):
        is_forbidden = request.user.is_authenticated or request.user.is_superuser
        has_wrong_pk = pk is not request.user.pk

        response = response.Response({})

        if pk is None or (is_forbidden and has_wrong_pk):
            response.status_code = 403
        else:
            response.status_code = 201

        logout(request)

        return response
