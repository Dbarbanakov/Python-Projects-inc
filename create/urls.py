from django.urls import path

from . import views

app_name = "create"

urlpatterns = [
    path("", views.index, name="index"),
    path("status/", views.status, name="status"),
    path("hero/<int:hero_id>", views.hero, name="hero"),
    path("added/", views.added, name="added"),
    # path("updated/<int:hero_id>/", views.updated, name="updated"),
    path("deleted/<int:hero_id>/", views.deleted, name="deleted"),
    path("saveandexit/", views.save_and_exit, name="saveandexit"),
]
