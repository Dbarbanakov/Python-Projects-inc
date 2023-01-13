from django.shortcuts import render, get_object_or_404
from .models import Hero
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
    if request.method == "POST":
        name = request.POST["name"]
        hero = get_object_or_404(Hero, pk=hero_id)
        hero.name = name
        hero.save()
    hero = get_object_or_404(Hero.objects.filter(pk=hero_id))
    return render(request, "create/hero.html", {"hero": hero, "form": form})


def status(request):
    if request.method == "POST":
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
