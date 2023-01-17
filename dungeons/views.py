from django.shortcuts import render, get_object_or_404
from django import forms

from create.models import Hero
from .models import Party


class NewFormMultiple(forms.Form):
    add_hero = forms.ModelMultipleChoiceField(queryset=Hero.objects.all())


def index(request):
    heroes = Hero.objects.all()
    return render(request, "dungeons/index.html", {"heroes": heroes})


def party(request):

    form = NewFormMultiple()
    parties = Party.objects.all()

    if request.method == "POST":
        if "delete" in request.POST:
            Party.objects.all().delete()
        if "create_party" in request.POST:
            party_id = request.POST["create_party"]
            party = Party()
            party.member = get_object_or_404(Hero, pk=party_id)
            party.save()

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
            Party.objects.create()
    return render(
        request,
        "dungeons/party.html",
        {"form": form, "parties": parties},
    )
