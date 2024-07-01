from django.urls import path
from post import views

urlpatterns = [
    path("home", views.home, name="home"),
    path("messages", views.messages, name="messages"),
    path("profile", views.profile, name="profile"),
    path("login", views.login, name="login"),
    path("signup", views.signup, name="signup"),
]
