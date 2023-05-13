from typing import Any
from django.db import models

from time import time, mktime
from datetime import datetime


class Avatar(models.Model):
    avatar = models.ImageField(upload_to="avatars")
    name = models.CharField(max_length=32)

    def __str__(self):
        return f"{self.name}"


class Party(models.Model):
    name = models.CharField(max_length=32, default="Party")

    def __str__(self):
        return f"{self.name}"


class Hero(models.Model):
    name = models.CharField(max_length=32)
    created = models.DateTimeField(default=datetime.now())
    avatar = models.ForeignKey(Avatar, on_delete=models.CASCADE, blank=True, null=True)
    party = models.ForeignKey(Party, on_delete=models.SET_NULL, blank=True, null=True)
    party_member = models.BooleanField(default=False)

    def exp(self):
        """Returns experience gained so far since time created."""
        return int(time() - mktime(self.created.timetuple()))

    def level(self):
        """Level 1 - 10k,Level 7 - 70k, each level needs 10k more exp than the previous."""
        level = 1
        base = 10000

        while Hero.exp(self) > base:
            level += 1
            base += 10000 * level

        return level

    def exp_percentage(self):
        """Returns the percentage needed for the experience bar."""
        max_exp_this_level = Hero.level(self) * 10000

        # Divides exp to level up with max xp for this level.
        exp_coeff = Hero.exp_to_level_up(self) / max_exp_this_level

        # Creates a 0 < number < 100 from the exp coefficient.
        percentage = (1 - exp_coeff) * 100

        # Rounds the number with 2 digits after the decimal.
        return round(percentage, 2)

    def exp_to_level_up(self):
        """Returns the experience needed for level up."""
        total_exp = 0

        # Calculates the total exp for this level.
        for i in range(Hero.level(self) + 1):
            total_exp += 10000 * i

        # Difference between total and current exp.
        return total_exp - Hero.exp(self)

    def level_up_date(self):
        """Returns the date on which the level up will occur."""

        # for this level or the time range from creation up until the moment of leveling up.
        total_exp = Hero.exp(self) + Hero.exp_to_level_up(self)

        # Adds the time range till creation with the one from creation till level up.
        x = int((mktime(self.created.timetuple())) + total_exp)

        # Converts the sum to a date.
        return datetime.fromtimestamp(x)

    def __str__(self):
        return f"{self.name}"
