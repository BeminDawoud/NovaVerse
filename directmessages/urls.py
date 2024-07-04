from django.urls import path
from directmessages import views


urlpatterns = [
    path("inbox", views.inbox, name="inbox"),
]
