from django.db import models
from create.models import Hero


class Party(models.Model):
    member = models.ForeignKey(Hero, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.member}"
