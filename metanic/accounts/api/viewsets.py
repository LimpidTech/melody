from django import http
from django.conf import settings
from django.contrib.auth import logout
from django.contrib.auth import models as auth_models
from django.utils import decorators
from django.views.decorators import csrf
from django import urls

from rest_framework import authentication as rest_authentication
from rest_framework import generics
from rest_framework import response
from rest_framework import viewsets
from rest_framework_jwt import authentication as jwt_authentication

from metanic.accounts import authentication
from metanic.rest import throttling

from . import serializers

METANIC_REDIRECT_URL = getattr(settings, 'METANIC_REDIRECT_URL', '/')

ensure_csrf = decorators.method_decorator(csrf.ensure_csrf_cookie)


def get_redirect_url(uri):
    if not uri:
        return None

    if uri.startswith('/'):
        uri = uri[1:]

    if uri and not uri.endswith('/'):
        uri += '/'

    return METANIC_REDIRECT_URL + uri


class UserViewSet(viewsets.ModelViewSet):
    queryset = auth_models.User.objects.all()
    serializer_class = serializers.UserSerializer

    def get_permissions(self):
        """ Override permissions so that unauthenticated users can create accounts. """

        if self.action == 'create':
            return []

        return super(UserViewSet, self).get_permissions()

    def filter_queryset(self, queryset):
        """ Ensure that users can not view details for other users. """

        if self.request.user.is_superuser:
            return queryset

        return queryset.filter(pk=self.request.user.pk)

    def retrieve(self, request, pk):
        """ Get user information. """

        if request.user.is_authenticated and pk == 'current':
            return http.HttpResponseRedirect(
                redirect_to=urls.
                reverse('user-detail', kwargs={
                    'pk': self.request.user.pk,
                })
            )

        return super(UserViewSet, self).retrieve(request, pk)


class AuthenticationViewSet(viewsets.ViewSet, generics.GenericAPIView):
    permission_classes = ()
    serializer_class = serializers.AuthenticationSerializer

    authentication_classes = (
        authentication.CSRFExemptAuthentication,
        jwt_authentication.JSONWebTokenAuthentication,
        rest_authentication.TokenAuthentication,
    )

    throttle_classes = (throttling.SensitiveDataRateThrottle,)

    @ensure_csrf
    def create(self, request):
        logout(request)

        input_serializer = self.get_serializer(data=request.data)
        redirect_url = get_redirect_url(request.data.get('redirect_uri'))

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
            input_serializer.validated_data['username'],
            input_serializer.validated_data['password'],
        )

        # TODO: Forwarding of error data
        if user is None:
            return response.Response({'username': None}, status=401)

        if redirect_url is not None:
            return http.HttpResponseRedirect(redirect_url)

        return response.Response(input_serializer.data, status=200)

    @ensure_csrf
    def destroy(self, request, pk=None):
        is_forbidden = request.user.is_authenticated
        has_wrong_pk = pk is not request.user.pk

        if pk is None or (is_forbidden and has_wrong_pk):
            return http.HttpResponseForbidden()

        logout(request)

        return response.Response({}, status=201)
