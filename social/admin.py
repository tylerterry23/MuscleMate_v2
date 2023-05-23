from django.contrib import admin
from .models import Post, Media, Comment, Like, View, Share

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('author', 'timestamp', 'content')
    search_fields = ('author__user__username', 'content')
    list_filter = ('timestamp',)

@admin.register(Media)
class MediaAdmin(admin.ModelAdmin):
    list_display = ('image', 'video', 'display_posts')

    def display_posts(self, obj):
        return ", ".join([str(post.id) for post in obj.post_set.all()])
    display_posts.short_description = 'Posts'


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('post', 'user', 'content', 'created_at')
    search_fields = ('post__content', 'user__user__username', 'content')
    list_filter = ('created_at',)

@admin.register(Like)
class LikeAdmin(admin.ModelAdmin):
    list_display = ('post', 'user', 'created_at')
    list_filter = ('created_at',)

@admin.register(View)
class ViewAdmin(admin.ModelAdmin):
    list_display = ('post', 'user', 'created_at')
    list_filter = ('created_at',)

@admin.register(Share)
class ShareAdmin(admin.ModelAdmin):
    list_display = ('post', 'user', 'created_at')
    list_filter = ('created_at',)
