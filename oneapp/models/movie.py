from django.db import models
from .actor import Actor


class Movie(models.Model):
    name = models.CharField(max_length=150, blank=False, null=False)
    year = models.IntegerField(blank=False,null=False)
    imdb = models.IntegerField(blank=False,null=False)
    genre = models.CharField(max_length=150, blank=False, null=False)
    actor = models.ManyToManyField('oneapp.Actor')


    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name