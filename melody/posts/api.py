from rest_framework import serializers, viewsets

from melody.rest import routing

from . import models

class PostSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        depth = 2
        model = models.Post
        fields = ('url', 'subject', 'body', 'categories')

class PostViewSet(viewsets.ModelViewSet):
    queryset = models.Post.objects.all()
    serializer_class = PostSerializer

routing.router.register(r'posts', PostViewSet)

class CategorySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        depth = 2
        model = models.Category
        fields = ('url', 'name', 'posts')

class CategoryViewSet(viewsets.ModelViewSet):
    queryset = models.Post.objects.all()
    serializer_class = PostSerializer

routing.router.register(r'categories', CategoryViewSet)
