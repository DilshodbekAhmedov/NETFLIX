from django.db import models
from django.contrib.auth import get_user_model
from .movie import Movie

User = get_user_model()


class Comment(models.Model):

    NEW = 'new'
    FINISHED = 'finished'

    STATUS = [
        (NEW, "new"),
        (FINISHED, "finished"),
    ]
    movie_id = models.ForeignKey('oneapp.Movie', on_delete=models.CASCADE)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField()
    created_data = models.DateField()

    def __str__(self):
        return self.text

    def mark_as_finished(self):
        self.status = self.FINISHED
        self.save()

    def mark_as_unfinished(self):
        self.status = self.NEW
        self.save()
