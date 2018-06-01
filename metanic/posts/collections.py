from zope import interface

from metanic.collector import collection
from metanic.posts import models as posts_models


@interface.implementer(collection.ICollection)
class RecentPostsCollection(collection.Collection):
    name = 'recent_posts'

    def __init__(self):
        super(RecentPostsCollection, self).__init__()
        self.pk = self.__class__.name

    def items(self, request):
        return posts_models.Post.objects.all()[:10]
