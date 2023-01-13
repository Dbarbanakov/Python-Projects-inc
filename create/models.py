from django.db import models

import datetime, time


class Avatar(models.Model):
    avatar = models.ImageField(upload_to="avatars")
    name = models.CharField(max_length=32)

    def __str__(self):
        return f"{self.name}"


class Hero(models.Model):

    name = models.CharField(max_length=32)
    avatar = models.ForeignKey(Avatar, on_delete=models.CASCADE, blank=True, null=True)
    created = models.DateTimeField(default=datetime.datetime.now())

    def exp(self):
        """Returns experience gained so far since time created."""
        now = datetime.datetime.now()
        return int(
            (time.mktime(now.timetuple())) - time.mktime(self.created.timetuple())
        )

    def current_next_level(self):
        """Returns a dictionary of current level as a key and experience to next level as a value."""
        exp = Hero.exp(self)
        base = 10000
        exp_increment = 10000
        current_level = 1

        while exp > base:
            current_level += 1
            base += exp_increment * current_level

        exp_to_next_level = base - exp

        return {current_level: exp_to_next_level}

    def __str__(self):
        return f"{self.name}"
