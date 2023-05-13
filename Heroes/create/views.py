from django.shortcuts import render, get_object_or_404

from django import forms

from .models import *


class HeroForm(forms.Form):
    name = forms.CharField(
        label="name", widget=forms.TextInput(attrs={"placeholder": "Choose a new name"})
    )


class PartyForm(forms.Form):
    hero_selection = forms.ModelMultipleChoiceField(
        queryset=Hero.objects.filter(party_member=False)
    )


def index(request):
    return render(request, "create/index.html")


def heroes(request):
    form = HeroForm()

    if request.method == "POST":
        if request.POST["name"]:
            new_hero = Hero(name=request.POST["name"])

        new_hero.save()

    heroes = Hero.objects.all()

    return render(request, "create/heroes.html", {"heroes": heroes, "form": form})


def hero(request, hero_id):
    form = HeroForm()
    avatars = Avatar.objects.all()
    hero = get_object_or_404(Hero, pk=hero_id)

    if request.method == "POST":
        if "new_avatar" in request.POST:
            hero.avatar = Avatar.objects.get(id=request.POST["new_avatar"])

        if "name" in request.POST:
            hero.name = request.POST["name"]

        if "detele" in request.POST:
            pass

    hero.save()
    hero = get_object_or_404(Hero.objects.filter(pk=hero_id))

    return render(
        request,
        "create/hero.html",
        {"hero": hero, "form": form, "avatars": avatars},
    )


def deleted(request, hero_id):
    hero = get_object_or_404(Hero, pk=hero_id)
    name = hero.name
    hero.delete()

    return render(request, "create/deleted.html", {"name": name})


def party(request):
    form = PartyForm()

    if request.method == "POST":
        if "hero_selection" in request.POST:
            party = (
                Party.objects.last()
                if Party.objects.exists()
                else Party.objects.create()
            )

            for id in request.POST.getlist("hero_selection"):
                hero = get_object_or_404(Hero, pk=id)

                party = (
                    Party.objects.last()
                    if party.hero_set.all().count() < 4
                    else Party.objects.create()
                )

                hero.party = party
                hero.party_member = True
                hero.save()

        if "delete" in request.POST:
            if Party.objects.exists():
                party = get_object_or_404(Party, pk=request.POST["delete"])

                for hero in party.hero_set.all():
                    hero.party_member = False
                    hero.save()

                party.delete()

    parties = Party.objects.all() if Party.objects.exists() else []

    return render(
        request,
        "create/party.html",
        {"form": form, "parties": parties},
    )
