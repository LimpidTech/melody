from rest_framework import serializers

from django.contrib.auth import models as auth_models


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta(object):
        model = auth_models.User

        fields = (
            'url',
            'username',
            'email',
        )


class AuthenticationSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField(write_only=True)
