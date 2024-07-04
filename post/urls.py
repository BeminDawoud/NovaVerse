from django.urls import path
from post import views

urlpatterns = [
    path("", views.home, name="home"),
    path("newpost", views.newPost, name="new-post"),
    path("post/<uuid:post_id>", views.postDetail, name="post-detail"),
    path("<uuid:post_id>/like", views.like, name="like"),
    path("favourite/<uuid:post_id>/", views.favourite, name="favourite"),
    path("saved/", views.bookmark, name="saved"),
    path("login", views.login, name="login"),
    path("signup", views.signup, name="signup"),
]
