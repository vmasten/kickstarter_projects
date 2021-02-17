"""Models for the Kickstarter project."""
from django.db import models


class Project(models.Model):
    """Model to store Kickstarter project data."""
    # name = models.CharField(max_length=128, default='name')
    category = models.CharField(max_length=64, default='cat')
    # main_category = models.CharField(max_length=64, default='maincat')
    currency = models.CharField(max_length=64, default='USD')
    # state = models.CharField(max_length=16, default='state')
    country = models.CharField(max_length=64, default='US')
    # deadline = models.DateField(default='2020-2-20')
    # launched = models.DateTimeField(default='2020-2-20 12:12:12')
    # goal = models.FloatField(max_length=64, default='0.0')
    # pledged = models.FloatField(max_length=64, default='0.0')
    # backers = models.IntegerField(max_length=64, default='0')
    # usd_pledged = models.FloatField(max_length=64, default='0.0')
    # usd_pledged_real = models.FloatField(max_length=64, default='0.0')
    # usd_goal_real = models.FloatField(max_length=64, default='0.0')

    def __str__(self):
        pass
        # return '{}'.format(self.name)
