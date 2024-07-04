from django.urls import path
from userauth import views

urlpatterns = [
    path("<username>/", views.userProfile, name="profile"),
    path("<username>/follow/<option>", views.follow, name="follow"),
    path("edit", views.editProfile, name="edit-profile"),
]
