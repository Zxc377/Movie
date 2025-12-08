from django.urls import path, include
from rest_framework.routers import DefaultRouter, SimpleRouter
from .views import (
    UserViewSet, CountryListAPIView, CountryDetailAPIView, DirectorListAPIView,
    DirectorDetailSerializer, ActorListAPIView, ActorDetailAPIView,
    GenreListAPIView, GenreDetailAPIView, MovieListAPIView, MovieDetailAPIView,
    MovieLanguagesViewSet, MomentsViewSet, RatingViewSet,
    FavoriteViewSet, FavoriteMovieViewSet, HistoryViewSet, DirectorDetailAPIView
)

router = SimpleRouter()


router.register(r'users', UserViewSet)
router.register(r'languages', MovieLanguagesViewSet)
router.register(r'moments', MomentsViewSet)
router.register(r'ratings', RatingViewSet)
router.register(r'favorites', FavoriteViewSet)
router.register(r'favorite-movies', FavoriteMovieViewSet)
router.register(r'history', HistoryViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('movie/', MovieListAPIView.as_view(), name='movie_list'),
    path('movie/<int:pk>/', MovieDetailAPIView.as_view(), name='movie_detail'),
    path('country/', CountryListAPIView.as_view(), name='country_list'),
    path('country/<int:pk>/', CountryDetailAPIView.as_view(), name='country_detail'),
    path('director/', DirectorListAPIView.as_view(), name='director_list'),
    path('director/<int:pk>/', DirectorDetailAPIView.as_view(), name='director_detail'),
    path('actor/', ActorListAPIView.as_view(), name='actor_list'),
    path('actor/<int:pk>/', ActorDetailAPIView.as_view(), name='actor_detail'),
    path('genre/', GenreListAPIView.as_view(), name='genre_list'),
    path('genre/<int:pk>/', GenreDetailAPIView.as_view(), name='genre_detail'),

]
