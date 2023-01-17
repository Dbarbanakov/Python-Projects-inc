from django.shortcuts import render
from django import forms




def index(request):
    return render(request, "testing/index.html")


def test(request):
    return render(request, "testing/test.html")
