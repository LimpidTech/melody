import json

from django import http
from django.utils import timezone

from rest_framework import generics
from rest_framework import response
from rest_framework import viewsets

from melody.core import decorators

from melody.mail import models

from . import serializers

# TODO: Add support for attachments


class BaseMailViewSet(viewsets.ViewSet, generics.GenericAPIView):
    permission_classes = ()

    def update_serializer_data(self, request, data):
        pass

    def get_initial_serializer_data(self, request):
        event_time = timezone.datetime.fromtimestamp(
            int(request.data['timestamp']),
        )

        return {
            'event': request.data['event'],
            'timestamp': event_time,
            'recipient': request.data['recipient'],
        }

    def store_mail_data(self, data):
        """ Attempts to insert the given data into the database.

        Inserts the given data into the mail log database. If the token is
        already present in the database, we raise a forbidden response
        because the request is a replay attack in this case.

        """

        token = data.get('token')

        try:
            models.MailEventLogModel.objects.get(token=token)
        except models.MailEventLogModel.DoesNotExist:
            models.MailEventLogModel.objects.create(
                token=token,
                raw_data=json.dumps(data),
            )
        else:
            return http.response.HttpResponseForbidden(
                'Token already exists. This is a replay attack.'
            )

    @decorators.signature_required()
    def create(self, request, action=None):
        storage_response = self.store_mail_data(request.data)

        if storage_response is not None:
            return storage_response

        data = self.get_initial_serializer_data(request)
        self.update_serializer_data(request, data)
        serializer = self.serializer_class(data=data)

        if not serializer.is_valid():
            return response.Response(
                status=400,
                data={
                    'request_data': request.data,
                    'errors': serializer.errors,
                },
            )

        return response.Response(serializer.data)


class MailDeliveredViewSet(BaseMailViewSet):
    serializer_class = serializers.MailDeliveredSerializer

    def update_serializer_data(self, request, data):
        data.update(
            {
                'body': request.data['body-plain'],
                'domain': request.data['domain'],
                'message_id': request.data['Message-Id'],
                'message_headers': request.data['message-headers'],
            }
        )


class MailDroppedViewSet(MailDeliveredViewSet):
    serializer_class = serializers.MailDroppedSerializer

    def update_serializer_data(self, request, data):
        super().update_serializer_data(request, data)

        data.update(
            {
                'code': request.data['code'],
                'description': request.data['description'],
                'reason': request.data['reason'],
            }
        )


class MailHardBouncedViewSet(MailDeliveredViewSet):
    serializer_class = serializers.MailHardBouncedSerializer

    def update_serializer_data(self, request, data):
        super().update_serializer_data(request, data)

        data.update({
            'error': request.data['error'],
        })


class MailSpamComplaintViewSet(MailDeliveredViewSet):
    serializer_class = serializers.MailSpamComplaintSerializer

    def update_serializer_data(self, request, data):
        super().update_serializer_data(request, data)


class LocationBasedEventMixin(object):
    def update_serializer_data(self, request, data):
        super().update_serializer_data(request, data)

        data.update(
            {
                'city': request.data['city'],
                'country': request.data['country'],
                'region': request.data['region'],
                'client_name': request.data['client-name'],
                'client_os': request.data['client-os'],
                'client_type': request.data['client-type'],
                'device_type': request.data['device-type'],
                'user_agent': request.data['user-agent'],
                'ip': request.data['ip'],
            }
        )


class MailUnsubscribeViewSet(LocationBasedEventMixin, BaseMailViewSet):
    serializer_class = serializers.GenericMailEventSerializer


class MailClickedViewSet(LocationBasedEventMixin, BaseMailViewSet):
    serializer_class = serializers.GenericMailEventSerializer
