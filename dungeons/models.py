from django.db import models
from create.models import Hero


class Party(models.Model):
    name = models.CharField(max_length=32, default="Party")
    member = models.ForeignKey(
        Hero, on_delete=models.CASCADE, default=Hero.objects.all().first()
    )

    def __str__(self):
        return f"{self.name}"
