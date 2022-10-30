from django.contrib import admin
from .models import movie, actor, comment


# Register your models here.
admin.site.register([movie.Movie,actor.Actor,comment.Comment])

