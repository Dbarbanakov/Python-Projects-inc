from django.urls import path

from . import views

app_name = "create"

urlpatterns = [
    path("", views.index, name="index"),
    path("status/", views.status, name="status"),
    path("saveandexit/", views.save_and_exit, name="saveandexit"),
    path("added/", views.added, name="added"),
    path("updated/<int:hero_id>/", views.updated, name="updated"),
    path("deleted/<int:hero_id>/", views.deleted, name="deleted"),
]
