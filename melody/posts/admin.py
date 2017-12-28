from django.contrib import admin

from . import models


class PostInline(admin.StackedInline):
    model = models.Post.topics.through
    extra = 3


class TopicAdmin(admin.ModelAdmin):
    list_display = ('name', 'last_modified', 'created', 'id')
    list_display_links = ('name',)

    list_filter = ('created', 'last_modified')
    search_fields = ('name',)

    inlines = [PostInline]

admin.site.register(models.Topic, TopicAdmin)


class TopicInline(admin.StackedInline):
    model = models.Topic.posts.through
    extra = 3


class PostAdmin(admin.ModelAdmin):
    list_display = ('subject', 'last_modified', 'created', 'id')
    list_display_links = ('subject',)

    list_filter = ('created', 'last_modified', 'topics')
    search_fields = ('subject', 'body')

    inlines = [TopicInline]


admin.site.register(models.Post, PostAdmin)
