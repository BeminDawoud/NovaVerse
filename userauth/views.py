from django.shortcuts import render, get_object_or_404
from django.contrib.auth.models import User
from django.urls import resolve
from post.models import Post, Follow
from userauth.models import Profile
from django.core.paginator import Paginator


# Create your views here.
def userProfile(request, username):
    user = get_object_or_404(User, username=username)
    profile = Profile.objects.get(user=user)
    posts = Post.objects.filter(user=user).order_by("-posted")

    # profile stats
    post_count = Post.objects.filter(user=user).count()
    following_count = Follow.objects.filter(follower=user).count()
    followers_count = Follow.objects.filter(following=user).count()

    context = {
        "posts": posts,
        "profile": profile,
        "post_count": post_count,
        "following_count": following_count,
        "followers_count": followers_count,
    }
    return render(request, "profile.html", context)
