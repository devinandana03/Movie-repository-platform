from django.urls import path
from movie.views import index, pagination, movieDetails, genres, addMoviesToWatch, addMoviesWatched, Rate, filter_view, filter_results


urlpatterns = [
    path('', index, name='index'),
    path('search/<query>/page/<page_number>', pagination, name='pagination'),
    path('<imdb_id>', movieDetails, name='movie-details'),
    path('<imdb_id>/addtomoviewatch', addMoviesToWatch, name='add-movies-to-watch'),
    path('<imdb_id>/addmoviewatched', addMoviesWatched, name='add-movies-watched'),
    path('genre/<slug:genre_slug>', genres, name='genres'),
    path('<imdb_id>/rate', Rate, name='rate-movie'),
    path('filter/', filter_view, name='filter'),
    path('filter_results/', filter_results, name='filter_results'),  # Add this line
    


]