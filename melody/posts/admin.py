from django.contrib import admin

from . import models


class CategoryInline(admin.StackedInline):
    model = models.Category.posts.through
    extra = 1


class PostAdmin(admin.ModelAdmin):
    list_display = ('subject', 'id')
    list_display_links = ('subject',)

    inlines = [
        CategoryInline,
    ]

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'id')
    list_display_links = ('name',)


admin.site.register(models.Post, PostAdmin)
admin.site.register(models.Category, CategoryAdmin)
