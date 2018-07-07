from metanic.accounts import api
from metanic.multisite.api import serializers as multisite_serializers
from metanic.rest import serializers
from metanic.posts import models


class PostSerializer(serializers.MetanicModelSerializer):
    author = api.serializers.AuthenticationSerializer(
        default=serializers.CurrentUserDefault(),
    )

    sites = multisite_serializers.SiteSerializer(
        many=True,
        read_only=True,
    )

    def save(self):
        request = self.context['request']
        instance = super(PostSerializer, self).save()

        # TODO: Although not using a "count" here to prevent a query,
        #       I think that calling all() will perform one anyway. We
        #       need to make sure that this is already materialized in
        #       the instance before this is called.
    
        if not len(instance.sites.all()):
            instance.sites.add(request.site)

        return instance

    class Meta(object):
        model = models.Post
        depth = 2

        fields = (
            'url',
            'local_reference',

            'subject',
            'html',
            'body',

            'author',

            'created',
            'last_modified',

            'sites',
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
