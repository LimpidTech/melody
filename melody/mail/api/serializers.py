from rest_framework import serializers

class MailOpenedSerializer(serializers.Serializer):
    event = serializers.CharField()
    timestamp = serializers.IntegerField()

    domain = serializers.CharField()
    body_plain = serializers.CharField(source='body-plain', null=True)

    city = serializers.CharField()
    country = serializers.CharField()
    region = serializers.CharField()

    client_name = serializers.CharField(source='client-name')
    client_os = serializers.CharField(source='client-os')
    client_type = serializers.CharField(source='client-type')
    device_type = serializers.CharField(source='device-type')
    user_agent = serializers.CharField(source='user-agent')

    ip = serializers.CharField()
    recipient = serializers.EmailField()
