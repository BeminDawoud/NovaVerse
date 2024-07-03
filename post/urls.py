from django.urls import path
from post import views

urlpatterns = [
    path("", views.home, name="home"),
    path("newpost", views.newPost, name="new-post"),
    path("post/<uuid:post_id>", views.postDetail, name="post-detail"),
    path("<uuid:post_id>/like", views.like, name="like"),
    path("messages", views.messages, name="messages"),
    path("profile", views.profile, name="profile"),
    path("login", views.login, name="login"),
    path("signup", views.signup, name="signup"),
]
