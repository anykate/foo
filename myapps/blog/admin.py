from django.contrib import admin
from .models import Topic, Post, Comment


# Register your models here.
class TopicAdmin(admin.ModelAdmin):
    pass


class PostAdmin(admin.ModelAdmin):
    pass


class CommentAdmin(admin.ModelAdmin):
    pass


admin.site.register(Topic, TopicAdmin)
admin.site.register(Post, PostAdmin)
admin.site.register(Comment, CommentAdmin)
