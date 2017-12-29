from rest_framework import serializers

from django.contrib.auth import models as auth_models


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta(object):
        model = auth_models.User

        fields = (
            'username',
            'email',
            'is_staff',
            'is_superuser',
        )


class AuthenticationSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()
