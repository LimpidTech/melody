from rest_framework import serializers

class MailSerializer(serializers.Serializer):
    type = serializers.CharField(source='event')
    timestamp = serializers.IntegerField()

    domain = serializers.CharField()

    recipient = serializers.CharField()
    message_id = serializers.CharField(source='Message-id')
    attachment_count = serializers.IntegerField(source='attachment-count')

    plain_text = serializers.CharField(source='body-plain')

    city = serializers.CharField()
    country = serializers.CharField()
    region = serializers.CharField()

    client_name = serializers.CharField(source='client-name')
    client_os = serializers.CharField(source='client-os')
    client_type = serializers.CharField(source='client-type')

    user_agent = serializers.CharField(source='user_agent')
    ip_address = serializers.CharField(source='ip')

    # message_headers = serializers.JSONField(source='message-headers')
    # code = serializers.IntegerField()
