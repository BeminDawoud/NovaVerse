from django.shortcuts import render
from post.models import Tag, Stream, Follow, Post
from django.contrib.auth.decorators import login_required

# Create your views here.


def home(request):
    user = request.user
    posts = Stream.objects.filter(user=user)
    group_ids = []
    for post in posts:
        group_ids.append(post.post_id)
    post_items = Post.objects.filter(id__in=group_ids).all().order_by("-posted")
    context = {
        "post_items": post_items,
    }
    return render(request, "home.html", context)


def messages(request):
    return render(request, "messages.html")


def profile(request):
    return render(request, "profile.html")


def login(request):
    return render(request, "login.html")


def signup(request):
    return render(request, "signup.html")
