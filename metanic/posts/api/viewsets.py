from rest_framework import viewsets

from metanic.posts import models

from . import serializers


class PostViewSet(viewsets.ModelViewSet):
    queryset = models.Post.objects.all()

    authentication_classes = ()
    serializer_class = serializers.PostSerializer


class TopicViewSet(viewsets.ModelViewSet):
    queryset = models.Topic.objects.all()

    authentication_classes = ()
    serializer_class = serializers.TopicSerializer
