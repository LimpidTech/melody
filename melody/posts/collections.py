from zope import interface

from melody.collector import collection
from melody.posts import models as posts_models


@interface.implementer(collection.ICollection)
class RecentPostsCollection(collection.Collection):
    name = 'recent_posts'

    def __init__(self, request):
        super(RecentPostsCollection, self).__init__(request=request)
        self.pk = self.__class__.name

    def items(self):
        return posts_models.Post.objects.all()[:10]
