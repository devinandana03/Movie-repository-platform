from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator
from django.template import loader
from django.http import HttpResponse

from actor.models import Actor
from movie.models import Movie
import imdb

# Create your views here.
def actors(request, actor_slug):
    actor = get_object_or_404(Actor, slug=actor_slug)
    movies = Movie.objects.filter(Actors=actor)
    ia = imdb.IMDb()
    imdb_person = ia.search_person(actor.name)
    if imdb_person:
        person = ia.get_person(imdb_person[0].personID)
        photo_url = person.get('full-size headshot')
    else:
        photo_url = None
    
    paginator = Paginator(movies, 9)
    page_number = request.GET.get('page')
    movie_data = paginator.get_page(page_number)
    
    context = {
        'movie_data' : movie_data,
        'actor' :actor,
        'photo_url': photo_url,
    }
    template = loader.get_template('actor.html')
    return HttpResponse(template.render(context, request))
# views.py
from django.shortcuts import render

def index(request):
    cards = [
        {'image': 'fallen.jpeg', 'title': 'AI Horizons', 'subtitle': 'Beyond Human Limits', 'meta': 'V1.0', 'description': 'Explore the future where AI transforms imagination into reality.'},
        # Add more cards to the list
    ]
    related_cards = [
        {'image': 'glass3d.gif', 'title': '3D Glass Portal Card Effect with React Three Fiber and Gaussian Splatting', 'url': 'https://tympanus.net/codrops/2023/11/29/3d-glass-portal-card-effect-with-react-three-fiber-and-gaussian-splatting/'},
        # Add more related cards to the list
    ]
    return render(request, 'index.html', {'cards': cards, 'related_cards': related_cards})

# urls.py
from django.urls import path
from. import views

urlpatterns = [
    path('', views.index, name='index'),
]