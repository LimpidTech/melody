from rest_framework import serializers

class MailOpenedSerializer(serializers.Serializer):
    # "ip": "50.56.129.169",
    # "my-var-2": "awesome",
    # "my_var_1": "Mailgun Variable #1",
    # "recipient": "alice@example.com",
    # "region": "CA",
    # "signature": "780c0a5bf645e17f3a9855c79eb020da51424c6c715704b36d073289f5618ff6",
    # "timestamp": "1515745813",
    # "token": "dd2183a27b9cb04f2280b80976b1ff02a8df5d75d8a60f703a",
    # "user-agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.31 (KHTML, like Gecko) Chrome/26.0.1410.43 Safari/537.31"

    event = serializers.CharField()
    timestamp = serializers.IntegerField()

    domain = serializers.CharField()
    body_plain = serializers.CharField(source='body-plain')

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
