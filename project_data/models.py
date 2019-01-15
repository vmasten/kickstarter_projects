"""Models for the Kickstarter project."""
from django.db import models


class Project(models.Model):
    """Model to store Kickstarter project data."""
    name = models.CharField(max_length=128)
    category = models.CharField(max_length=64)
    main_category = models.CharField(max_length=64)
    currency = models.CharField(max_length=16)
    state = models.CharField(max_length=16)
    country = models.CharField(max_length=4)
    deadline = models.DateField(default='2020-2-20')
    launched = models.DateTimeField(default='2020-2-20 12:12:12')
    goal = models.FloatField()
    pledged = models.FloatField()
    backers = models.IntegerField()
    usd_pledged = models.FloatField()
    usd_pledged_real = models.FloatField()
    usd_goal_real = models.FloatField()


    def __str__(self):
        return '{}'.format(self.title)
