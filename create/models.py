from django.db import models

import datetime, time


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
    created = models.DateTimeField(default=datetime.datetime.now())
    avatar = models.ForeignKey(Avatar, on_delete=models.CASCADE, blank=True, null=True)
    party = models.ForeignKey(Party, on_delete=models.SET_NULL, blank=True, null=True)
    party_member = models.BooleanField(default=False)

    def exp(self):
        """Returns experience gained so far since time created."""
        now = datetime.datetime.now()
        return int(time.mktime(now.timetuple()) - time.mktime(self.created.timetuple()))

    def current_level(self):
        """Returns the current hero level."""
        exp = Hero.exp(self)
        base = 10000
        exp_increment = 10000
        current_level = 1

        while exp > base:
            current_level += 1
            base += exp_increment * current_level
        return current_level

    def current_level_exp_percentage(self):
        """Returns the percentage needed for the experience bar."""
        percentage = 100 - (
            Hero.next_level_exp_total(self) - Hero.exp(self)
        ) * 100 / Hero.next_level_exp(self)
        return round(percentage, 2)

    def next_level_exp(self):
        """Returns the experience needed for level up.."""
        return Hero.current_level(self) * 10000

    def next_level_exp_total(self):
        """Returns the total experience needed for level up."""
        next_level_exp_total = 0
        for i in range(Hero.current_level(self) + 1):
            next_level_exp_total += 10000 * i
        return next_level_exp_total

    def next_level_date(self):
        """Returns the date on which the level up will occur."""
        date = Hero.next_level_exp_total(self)

        x = int((time.mktime(self.created.timetuple())) + date)

        next_level_date = datetime.datetime.fromtimestamp(x)
        return next_level_date

    def __str__(self):
        return f"{self.name}"
