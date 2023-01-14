from django.shortcuts import render, get_object_or_404
from .models import Hero, Avatar
from django import forms


class HeroForm(forms.Form):
    name = forms.CharField(
        label="name", widget=forms.TextInput(attrs={"placeholder": "Choose a new name"})
    )


def index(request):
    form = HeroForm()
    return render(request, "create/index.html", {"form": form})


def hero(request, hero_id):
    form = HeroForm()
    avatars = Avatar.objects.all()
    hero = get_object_or_404(Hero, pk=hero_id)
    if request.method == "POST":
        if "new_avatar" in request.POST:
            new_avatar = request.POST["new_avatar"]
            hero.avatar = Avatar.objects.get(id=new_avatar)
        if "name" in request.POST:
            name = request.POST["name"]
            hero.name = name

    hero.save()
    hero = get_object_or_404(Hero.objects.filter(pk=hero_id))
    return render(
        request,
        "create/hero.html",
        {"hero": hero, "form": form, "avatars": avatars},
    )


def status(request):
    if request.method == "POST":
        if request.POST["name"]:
            name = request.POST["name"]
            new_hero = Hero(name=name)
        new_hero.save()
    heroes = Hero.objects.all()
    return render(request, "create/status.html", {"heroes": heroes})


def save_and_exit(request):
    return render(request, "create/saveandexit.html")


def deleted(request, hero_id):
    hero = get_object_or_404(Hero, pk=hero_id)
    name = hero.name
    hero.delete()
    return render(request, "create/deleted.html", {"name": name})
