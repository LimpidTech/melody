from rest_framework import serializers

from melody.posts import models


class PostSerializer(serializers.HyperlinkedModelSerializer):
    class Meta(object):
        model = models.Post
        depth = 2

        fields = (
            'url',
            'body',
            'html',
            'subject',
            'topics',
        )


class TopicSerializer(serializers.HyperlinkedModelSerializer):
    class Meta(object):
        model = models.Topic
        depth = 2

        fields = (
            'url',
            'name',
            'posts',
        )
