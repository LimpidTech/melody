from rest_framework import serializers

from melody.posts import models


class PostSerializer(serializers.HyperlinkedModelSerializer):
    class Meta(object):
        model = models.Post
        depth = 2

        fields = (
            'url',
            'subject',
            'body',
            'categories',
        )


class CategorySerializer(serializers.HyperlinkedModelSerializer):
    class Meta(object):
        model = models.Category
        depth = 2

        fields = (
            'url',
            'name',
            'posts',
        )
