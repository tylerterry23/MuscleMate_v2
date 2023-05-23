from django.shortcuts import render
from .models import Post, Profile, Comment, Like, View, Share, Media
from django.db.models import Count

def home(request):
    return render(request, 'social/home.html')

def social_feed(request):
    posts = Post.objects.all().order_by('-timestamp').annotate(
        comments_count_anno=Count('comments', distinct=True),
        likes_count_anno=Count('likes', distinct=True),
        views_count_anno=Count('views', distinct=True),
        shares_count_anno=Count('shares', distinct=True)
    ).prefetch_related('media')

    # get profile name from post username
    for post in posts:
        try:
            # based on post username, get profile name from Profile model
            profile = Profile.objects.get(user__username=post.author)
            post.profile_name = profile.name
        except Profile.DoesNotExist:
            post.profile_name = ""

    context = {
        'posts': posts,
    }

    return render(request, 'social/social_feed.html', context)
