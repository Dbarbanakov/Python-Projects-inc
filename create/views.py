from django.shortcuts import render
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
    if request.method == "POST":
        name = request.POST["name"]
        new_hero = Hero(name=name)
        new_hero.save()
    heroes = Hero.objects.all()
    return render(request, "create/added.html", {"heroes": heroes})
