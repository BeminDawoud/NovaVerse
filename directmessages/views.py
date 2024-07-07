from django.shortcuts import redirect, render, get_object_or_404
from django.contrib.auth.decorators import login_required
from directmessages.models import Message
from django.contrib.auth.models import User
from userauth.models import Profile
from post.models import Follow
from django.core.paginator import Paginator
from django.db.models import Q


# Create your views here.
@login_required
def inbox(request):
    user = request.user
    messages = Message.get_message(user=request.user)
    active_direct = None
    directs = None
    profile = get_object_or_404(Profile, user=user)

    if messages:
        message = messages[0]
        active_direct = message["user"].username
        directs = Message.objects.filter(user=request.user, reciepient=message["user"])
        directs.update(is_read=True)

        for message in messages:
            if message["user"].username == active_direct:
                message["unread"] = 0
    context = {
        "directs": directs,
        "messages": messages,
        "active_direct": active_direct,
        "profile": profile,
    }
    return render(request, "messages.html", context)


@login_required
def Directs(request, username):
    user = request.user
    messages = Message.get_message(user=user)
    active_direct = username
    directs = Message.objects.filter(user=user, reciepient__username=username)
    directs.update(is_read=True)

    for message in messages:
        if message["user"].username == username:
            message["unread"] = 0
    context = {
        "directs": directs,
        "messages": messages,
        "active_direct": active_direct,
    }
    return render(request, "direct.html", context)


def SendDirect(request):
    from_user = request.user
    to_user_username = request.POST.get("to_user")
    body = request.POST.get("body")

    if request.method == "POST":
        to_user = User.objects.get(username=to_user_username)
        Message.sender_message(from_user, to_user, body)
        return redirect("direct", username=to_user.username)
    else:
        pass


def NewMessage(request, username):
    from_user = request.user
    body = "Hey!"
    to_user = User.objects.get(username=username)
    if from_user != to_user:
        Message.sender_message(from_user, to_user, body)
    return redirect("direct", username=to_user.username)


def userSearch(request):
    query = request.GET.get("q")
    users_paginator = None  # Initialize users_paginator

    if query:
        users = User.objects.filter(Q(username__icontains=query))

        paginator = Paginator(users, 8)
        page_number = request.GET.get("page")
        users_paginator = paginator.get_page(page_number)

        for user in users_paginator:
            user.follow_status = Follow.objects.filter(
                follower=request.user, following=user
            ).exists()

    context = {
        "users": users_paginator,
    }
    return render(request, "search.html", context)
