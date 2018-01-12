from rest_framework import serializers

class MailSerializer(serializers.Serializer):
    event = serializers.CharField()
    timestamp = serializers.IntegerField()

    domain = serializers.CharField()
    code = serializers.IntegerField()

    recipient = serializers.CharField()
    message_id = serializers.CharField(source='Message-id')
    attachment_count = serializers.IntegerField(source='attachment-count')

    body_plain = serializers.CharField(source='body-plain')
    message_headers = serializers.JSONField(source='message-headers')
