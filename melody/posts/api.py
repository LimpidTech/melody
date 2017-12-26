from rest_framework import serializers, viewsets

from melody.rest import routing

from . import models

class PostSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.Post
        fields = ('url', 'subject', 'body')

class PostViewSet(viewsets.ModelViewSet):
    queryset = models.Post.objects.all()
    serializer_class = PostSerializer

routing.router.register(r'posts', PostViewSet)
