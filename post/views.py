from django.shortcuts import render

# Create your views here.


def home(request):
    return render(request, "home.html")


def messages(request):
    return render(request, "messages.html")


def profile(request):
    return render(request, "profile.html")


def login(request):
    return render(request, "login.html")


def signup(request):
    return render(request, "signup.html")
