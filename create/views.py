from django.shortcuts import render
from django import forms
from .models import Hero
from django.http import HttpResponseRedirect


class NewForm(forms.Form):
    health = forms.IntegerField(label="Health Points")


def index(request):
    if "stats" not in request.session:
        request.session["stats"] = []
    if request.method == "POST":
        form = NewForm(request.POST)
        if form.is_valid():
            hp = form.cleaned_data["health"]
            request.session["stats"] += [hp]
            return render(
                request, "create/stats.html", {"stats": request.session["stats"]}
            )
        else:
            return render(request, "create/index.html", {"form": form})
    return render(request, "create/index.html", {"form": NewForm()})


def stats(request):
    return render(request, "create/stats.html")


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
