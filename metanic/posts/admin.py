from django.contrib import admin

from . import models


class PostInline(admin.StackedInline):
    model = models.Post.topics.through
    extra = 3


class TopicAdmin(admin.ModelAdmin):
    list_display = ('name', 'last_modified', 'created')
    list_display_links = ('name',)

    list_filter = ('created', 'last_modified')
    search_fields = ('name',)

    inlines = [PostInline]


admin.site.register(models.Topic, TopicAdmin)


class CategoryAdmin(TopicAdmin):
    pass
    

admin.site.register(models.Category, CategoryAdmin)


class TopicInline(admin.StackedInline):
    model = models.Post.topics.through
    extra = 3


class CategoryInline(admin.StackedInline):
    model = models.Post.categories.through
    extra = 1


class PostAdmin(admin.ModelAdmin):
    list_display = ('subject', 'last_modified', 'created', 'id')
    list_display_links = ('subject',)

    list_filter = ('created', 'last_modified', 'topics', 'categories')
    search_fields = ('subject', 'body')

    inlines = (TopicInline, CategoryInline)


admin.site.register(models.Post, PostAdmin)
