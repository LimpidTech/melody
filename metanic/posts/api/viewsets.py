from metanic.posts import models
from metanic.rest import viewsets

from . import serializers


class PostViewSet(viewsets.MetanicModelViewSet):
    queryset = models.Post.objects.all()
    serializer_class = serializers.PostSerializer


class TopicViewSet(viewsets.MetanicModelViewSet):
    queryset = models.Topic.objects.all()
    serializer_class = serializers.TopicSerializer