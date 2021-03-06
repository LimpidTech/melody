from metanic.rest import serializers

from metanic.accounts import models


class UserSerializer(serializers.MetanicModelSerializer):
    email = serializers.EmailField()

    # TODO: When we write unit tests, ensure that these are write_only in specific tests.
    password = serializers.CharField(write_only=True)
    password_verification = serializers.CharField(write_only=True)

    username = serializers.CharField()

    def validate(self, data):
        password = data['password']
        password_verification = data['password_verification']

        if password and password != password_verification:
            return serializers.ValidationError(
                "The verification password must be the same as the password."
            )

        return super(UserSerializer, self).validate(data)

    class Meta(serializers.MetanicModelSerializer.Meta):
        model = models.User

        fields = (
            'url',
            'local_reference',
            'username',
            'email',
            'password',
            'password_verification',
        )


class AuthenticationSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField(write_only=True)
