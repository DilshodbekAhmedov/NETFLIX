from django.test import TestCase,Client

from oneapp.models.movie import Movie
from oneapp.serializers import MovieSerializer


class TestMovieViewSet(TestCase):
    def setUp(self) -> None:
        self.client = Client()
        self.movie1 = Movie.objects.create(name = "Yitti haykal bir kal",year = "2015",imdb = 10,genre ="kamidiya")
        self.movie2 = Movie.objects.create(name="Jaxon Afsonasi", year="2022", imdb=11, genre="drama")

    def test_movie_search(self):
        response = self.client.get('/movies/?ordering=-imdb')
        data = response.data
        assert data[0]['imdb'] == 11
        print(data[0]['imdb'])
