from django.db import models


class Director(models.Model):
    name = models.CharField(max_length=32)

    def __str__(self):
        return f"{self.name}"


class Movie(models.Model):
    name = models.CharField(max_length=32)
    director = models.ForeignKey(Director, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.name}"
