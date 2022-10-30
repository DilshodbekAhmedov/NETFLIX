from django.test import TestCase,Client

from oneapp.models.movie import Movie
from oneapp.serializers import MovieSerializer


class TestMovieViewSet(TestCase):
    def setUp(self) -> None:
        self.client = Client()
        self.movie1 = Movie.objects.create(name = "Yitti haykal bir kal",year = "2015",imdb = 10,genre ="kamidiya")
        self.movie2 = Movie.objects.create(name="Jaxon Afsonasi", year="2022", imdb=11, genre="drama")

    def test_data_returned_movie(self):
        data1 = MovieSerializer(self.movie1).data
        data2 = MovieSerializer(self.movie2).data
        # print(data1)
        assert data1["id"] is not None

        response = self.client.get('/movies/')
        data = response.data
        self.assertEqual(response.status_code, 200)
        # print(data)
        self.assertEqual(len(data1), 6)

    def test_movie_search(self):
        response = self.client.get('/movies/?search=Yitti')
        data = response.data
        assert data[0]['name'] == 'Yitti haykal bir kal'