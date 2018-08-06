from metanic.accounts import api
from metanic.multisite.api import serializers as multisite_serializers
from metanic.rest import serializers
from metanic.posts import models


class BasePostSerializer(serializers.MetanicModelSerializer):
    """ This needs to exist so that Topic and Post can reference eachother. """

    author = api.serializers.UserSerializer(
        default=serializers.CurrentUserDefault(),
    )

    sites = multisite_serializers.SiteSerializer(
        many=True,
        read_only=True,
    )

    def run_validation(self, data=serializers.empty):
        topics = data.get('topics', [])

        if isinstance(topics, str):
            data['topics'] = []

            for topic in models.Topic.objects.having_names(
                    topics, create_missing=True):
                data['topics'].append(
                    TopicSerializer(
                        topic,
                        context=self.context,
                    ).data
                )

        return super(BasePostSerializer, self).run_validation(data=data)

    def save(self):
        request = self.context['request']
        instance = super(BasePostSerializer, self).save()

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
            'topics',
            'is_pinned',
        )


# TODO: Figure out how to have Topic <--> Post happily
class TopicSerializer(serializers.MetanicModelSerializer):
    posts = BasePostSerializer(many=True, read_only=True)

    class Meta(object):
        model = models.Topic
        depth = 2

        fields = (
            'url',
            'local_reference',
            'name',
            'posts',
            'created',
            'last_modified',
        )


class PostSerializer(BasePostSerializer):
    # TODO: Fix saving topics (nested modelds w/ hyperlinked URLs seem broken)
    topics = TopicSerializer(many=True, read_only=True)
