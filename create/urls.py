from django.urls import path

from . import views

app_name = "create"

urlpatterns = [
    path("", views.index, name="index"),
    path("heroes/", views.heroes, name="heroes"),
    path("hero/<int:hero_id>", views.hero, name="hero"),
    path("deleted/<int:hero_id>/", views.deleted, name="deleted"),
    path("party/", views.party, name="party"),
]
