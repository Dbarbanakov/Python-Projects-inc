from django.db import models


class Party(models.Model):
    name = models.CharField(max_length=32, default="Party")

    def __str__(self):
        return f"{self.name}"
