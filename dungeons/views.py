from django.shortcuts import render, get_object_or_404
from django import forms

from create.models import Hero
from .models import Party


class NewFormMultiple(forms.Form):
    hero_selection = forms.ModelMultipleChoiceField(
        queryset=Hero.objects.filter(party_member=False)
    )


def index(request):
    heroes = Hero.objects.all()
    return render(request, "dungeons/index.html", {"heroes": heroes})


def party(request):

    form = NewFormMultiple()

    if request.method == "POST":

        if "hero_selection" in request.POST:
            if not Party.objects.exists():
                party = Party.objects.create()
            party = Party.objects.last()
            hero_ids = request.POST.getlist("hero_selection")
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
            if Party.objects.exists():
                party_id = request.POST["delete"]
                party = Party.objects.get(pk=party_id)
                for hero in party.hero_set.all():
                    hero.party_member = False
                    hero.save()
                party.delete()

    if Party.objects.exists():
        parties = Party.objects.all()
    else:
        parties = []

    return render(
        request,
        "dungeons/party.html",
        {"form": form, "parties": parties},
    )
