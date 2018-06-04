from zope import interface

from metanic.collector import collection
from metanic.posts import models as posts_models


@interface.implementer(collection.ICollection)
class RecentPostsCollection(collection.Collection):
    name = 'recent_posts'

    def items(self, request):
        return posts_models.Post.objects.all()[:10]
