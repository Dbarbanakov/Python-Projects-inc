from django.shortcuts import render, get_object_or_404
from .models import Hero
from django import forms


class HeroForm(forms.Form):
    name = forms.CharField(max_length=32)


def index(request):
    form = HeroForm()
    return render(request, "create/index.html", {"form": form})


def status(request):
    exp_dict = {}
    exp_pack = {}
    for hero in Hero.objects.all():
        exp = hero.exp()
        level = hero.current_level()
        exp_pack[level] = exp
        exp_dict[hero] = exp_pack
        exp_pack = {}
    return render(
        request,
        "create/status.html",
        {"experience": exp_dict},
    )


def save_and_exit(request):
    return render(request, "create/saveandexit.html")


def added(request):
    form = HeroForm()
    if request.method == "POST":
        name = request.POST["name"]
        new_hero = Hero(name=name)
        new_hero.save()
    heroes = Hero.objects.all()
    return render(request, "create/added.html", {"heroes": heroes, "form": form})


def updated(request, hero_id):
    name = request.POST["name"]
    hero = get_object_or_404(Hero, pk=hero_id)
    hero.name = name
    hero.save()
    return render(request, "create/updated.html", {"hero": hero})


def deleted(request, hero_id):
    hero = get_object_or_404(Hero, pk=hero_id)
    name = hero.name
    hero.delete()
    return render(request, 'create/deleted.html', {'name': name})
