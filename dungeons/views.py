from django.shortcuts import render, get_object_or_404
from django import forms

from create.models import Hero
from .models import Party


class NewFormMultiple(forms.Form):
    add_hero = forms.ModelMultipleChoiceField(
        queryset=Hero.objects.filter(party_member=False)
    )


def index(request):
    heroes = Hero.objects.all()
    return render(request, "dungeons/index.html", {"heroes": heroes})


def party(request):

    form = NewFormMultiple()
    parties = Party.objects.all()

    if request.method == "POST":

        if "add_hero" in request.POST:
            hero_ids = request.POST.getlist("add_hero")
            heroes = []
            for i in hero_ids:
                hero = get_object_or_404(Hero, pk=i)
                heroes.append(hero)
            return render(
                request,
                "dungeons/party.html",
                {"form": form, "parties": parties, "heroes": heroes},
            )

        if "add_to_party" in request.POST:
            if not Party.objects.all():
                party = Party.objects.create()

            party = Party.objects.last()

            hero_ids = request.POST.getlist("add_to_party")

            for i in hero_ids:
                hero = get_object_or_404(Hero, pk=i)
                if party.hero_set.all().count() < 4:
                    party = Party.objects.last()
                else:
                    party = Party.objects.create()
                hero.party = party
                hero.party_member = True
                hero.save()

        if "delete" in request.POST:
            Party.objects.all().delete()
            for hero in Hero.objects.filter(party_member=True):
                hero.party_member = False
                hero.save()

    return render(
        request,
        "dungeons/party.html",
        {"form": form, "parties": parties},
    )
