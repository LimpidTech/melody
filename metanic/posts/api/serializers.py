from rest_framework import serializers

from metanic.posts import models
from metanic.accounts import api


class PostSerializer(serializers.HyperlinkedModelSerializer):
    author = api.serializers.AuthenticationSerializer(
        default=serializers.CurrentUserDefault(),
    )

    class Meta(object):
        model = models.Post
        deth = 2

        fields = (
            'url',
            'body',
            'html',
            'subject',
            'author',
            'created',
            'last_modified',
        )


class TopicSerializer(serializers.HyperlinkedModelSerializer):
    class Meta(object):
        model = models.Topic
        depth = 2

        fields = (
            'url',
            'name',
            'posts',
            'created',
            'last_modified',
        )
