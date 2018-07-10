import typing

from django.db.models import Manager
from django.db.models.query import QuerySet


class TopicManager(Manager):
    def having_names(self, names: str, *, create_missing: bool = False, **create_kwargs: typing.Dict[str, typing.Any]) -> QuerySet:
        if not len(names):
            return self.none()

        topic_names = set(map(str.strip, names.lower().split(',')))

        # TODO: Support use directly as QuerySet
        related_topics = self.all()

        for name in topic_names:
            related_topics |= related_topics.filter(name__iexact=name)

        if create_missing and len(related_topics) != len(topic_names):
            missing_topics = topic_names.difference([topic.name for topic in related_topics])
            topics_to_create = []
        
            for name in missing_topics:
                topic = self.model(name=name, **create_kwargs)
                topic.prepare_for_save()
                topics_to_create.append(topic)

            related_topics |= self.filter(pk__in=[
                topic.pk
                for topic in self.bulk_create(topics_to_create)
            ])

        return related_topics