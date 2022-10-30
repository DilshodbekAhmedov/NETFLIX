import datetime
from rest_framework.viewsets import ModelViewSet

from rest_framework import serializers
from .models.movie import Movie
from .models.actor import Actor
from .models.comment import Comment
from rest_framework.exceptions import ValidationError


class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = ('id', 'name', 'year', 'imdb', 'genre', 'actor')


class ActorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Actor
        fields = ('id', 'name', 'birthdate', 'genre')

    def validate_birthdate(self, value):
        print(type(value))
        if value < datetime.date(1950, 1, 1):
            raise ValidationError(detail='Bu sanadan kattaroq kriting')

        return value


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'
