from django.shortcuts import render
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from .models.movie import Movie
from .models.actor import Actor
from .models.comment import Comment
from .serializers import MovieSerializer, ActorSerializer, CommentSerializer
from rest_framework.viewsets import ModelViewSet
from rest_framework.decorators import action
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework import filters
from django_filters.rest_framework import DjangoFilterBackend

# Create your views here.

# class ActorAPIView(APIView):
#     def get(self, request):
#         actor = Actor.objects.all()
#         serializer = ActorSerializer(actor,many=True)
#         return Response(data=serializer.data)
#
#     def post(self, request):
#         serializer = ActorSerializer(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         actor = serializer.save()
#
#         return Response(data=serializer.data)

class ActorViewSet(ModelViewSet):
    queryset = Actor.objects.all()
    serializer_class = ActorSerializer


#
# class MovieAPIView(APIView):
#     def get(self, request):
#         movie = Movie.objects.all()
#         serializer = MovieSerializer(movie,many=True)
#         return Response(data=serializer.data)
#
#     def post(self, request):
#         serializer = MovieSerializer(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         movie = serializer.save()
#
#         return Response(data=serializer.data)




class MovieViewSet(ModelViewSet):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = 'genre',
    search_fields = 'name',
    ordering_fields = ['imdb', '-imdb']



    @action(detail=True, methods=["POST"])
    def add_actor(self, request, *args, **kwargs):
        movie = self.get_object()
        name = request.data['name']
        birthdate = request.data['birthdate']
        genre = request.data['genre']
        id = request.data["id"]
        # print(type(id))
        if id == 0:
            new_actor = Actor.objects.create(name=name, birthdate=birthdate, genre=genre)
            movie.actor.add(new_actor)
        else:
            existed_actors = Actor.objects.filter(id=id)
            if len(existed_actors) == 0:
                return Response(status=status.HTTP_404_NOT_FOUND)
            existed_actor = existed_actors[0]
            movie.actor.add(existed_actor)
        movie.save()
        return Response(status=status.HTTP_204_NO_CONTENT)

    @action(detail=True, methods=['POST'])
    def remove_actor(self, request, *args, **kwargs):
        movie = self.get_object()
        id = request.data["id"]
        try:
            r_actor = Actor.objects.filter(id=id)
            movie.actor.remove(r_actor[0])
            movie.save()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except:
            return Response(status=status.HTTP_404_NOT_FOUND)

# class MovieActorAPIView(APIView):
#
#     def get(self, request):
#         movie = Movie.objects.all()
#         serializer = MovieSerializer(movie,many=True)
#         return Response(data=serializer.data)


class CommentAPIView(APIView):
    permission_classes = (IsAuthenticated,)
    authentication_classes = (TokenAuthentication,)

    def get(self, request):

        comment = Comment.objects.all()
        serializer = CommentSerializer(comment,many=True)
        return Response(data=serializer.data)


    def post(self, request):

        serializer = CommentSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        text = serializer.save()

        return Response(data=serializer.data)

    def delete(self, request, *args, **kwargs):
        comment = self.get_objects()
        id = request.data['id']

        comments = Comment.objects.filter(id=id)
        comm = comments[0]
        comment.delete(comm)

        return Response(status=status.HTTP_204_NO_CONTENT)
