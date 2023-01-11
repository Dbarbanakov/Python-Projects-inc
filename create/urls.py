from django.urls import path

from . import views

app_name = "create"

urlpatterns = [
    path("", views.index, name="index"),
    path("added/", views.added, name="added"),
    path("status/", views.status, name="status"),
    path("saveandexit/", views.save_and_exit, name="saveandexit"),
]
