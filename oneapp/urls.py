from .views import MovieViewSet, ActorViewSet,CommentAPIView
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken.views import obtain_auth_token

router = DefaultRouter()

router.register('movies', MovieViewSet)
router.register('actors', ActorViewSet)

urlpatterns = [
    # path('<int:pk>/actors/',MovieActorAPIView.as_view(), name='movie_actors'),
    path('', include(router.urls)),
    path('auth/',obtain_auth_token),
    path('add_comment/',CommentAPIView.as_view()),
    path('del/{int:pk}',CommentAPIView.as_view(), name='delete_event'),
]
