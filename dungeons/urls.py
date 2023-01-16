from django.urls import path

from . import views

app_name = "dungeons"

urlpatterns = [
    path("", views.index, name="index"),
    path("party/", views.party, name="party"),
]
