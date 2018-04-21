from rest_framework import serializers


class BaseMailSerializer(serializers.Serializer):
    event = serializers.CharField()
    timestamp = serializers.DateTimeField()


class BaseEnvelopeSerializer(BaseMailSerializer):
    recipient = serializers.CharField()
    body = serializers.CharField(allow_blank=True)
    domain = serializers.CharField()
    event = serializers.CharField()
    message_id = serializers.CharField()


class MailDeliveredSerializer(BaseEnvelopeSerializer):
    pass


class MailDroppedSerializer(MailDeliveredSerializer):
    description = serializers.CharField()
    code = serializers.IntegerField()
    reason = serializers.CharField()


class MailHardBouncedSerializer(MailDeliveredSerializer):
    error = serializers.CharField()


class MailSpamComplaintSerializer(MailDeliveredSerializer):
    pass


class GenericMailEventSerializer(BaseMailSerializer):
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
