from django.shortcuts import render, get_object_or_404
from django import forms

from create.models import Hero
from .models import Party


class NewForm(forms.Form):
    choice = forms.ModelChoiceField(queryset=Hero.objects.all())


class NewFormMultiple(forms.Form):
    choices = forms.ModelMultipleChoiceField(queryset=Hero.objects.all())


def index(request):
    heroes = Hero.objects.all()
    return render(request, "dungeons/index.html", {"heroes": heroes})


def party(request):
    form = NewForm()
    form2 = NewFormMultiple()
    parties = Party.objects.all()

    if request.method == "POST":
        if "choice" in request.POST:
            choice = request.POST["choice"]
            party = Party()
            party.member = get_object_or_404(Hero, pk=choice)
            party.save()

        if "choices" in request.POST:
            choices = request.POST.getlist("choices")
            heroes = []
            for i in choices:
                hero = get_object_or_404(Hero, pk=i)
                heroes.append(hero)
            return render(
                request,
                "dungeons/party.html",
                {"form": form, "form2": form2, "parties": parties, "heroes": heroes},
            )
    return render(
        request,
        "dungeons/party.html",
        {"form": form, "form2": form2, "parties": parties},
    )
