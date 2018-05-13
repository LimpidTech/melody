from rest_framework import serializers

from django.contrib.auth import models as auth_models


class UserSerializer(serializers.HyperlinkedModelSerializer):
    email = serializers.EmailField()

    password = serializers.CharField(write_only=True)
    password_verification = serializers.CharField(write_only=True)

    username = serializers.CharField()

    def validate(self, data):
        if data['password'] != data['password_verification']:
            return serializers.ValidationError(
                "The verification password must be the same as the password."
            )

        return super(AuthenticationSerializer, self).is_valid()

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