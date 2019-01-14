from django.shortcuts import render, get_object_or_404
from .models import Review, Beer, Brewery, Category 
from django.contrib.auth.models import User
from django.urls import reverse, reverse_lazy
from django.views import generic


def index(request):
    return render(request, 'index.html')
    
def user_beer_list(request):
    
    user = request.user
    user_beers = Review.objects.filter(author=user)
    
    return render(request, 'beer/user_beers.html', {'user_beers':user_beers})
    
#def all_beers(request):
#    beers = Beer.objects.all().order_by('brewery', 'name')
#    return render(request, 'beer/all_beers.html', {'beers':beers})
#    
#def breweries(request):
#    breweries = Brewery.objects.all()
#    
#    return render(request, 'beer/brewery_list.html', {'breweries': breweries})
    
class BeerListView(generic.ListView):
    model = Beer
  
class BeerDetailView(generic.DetailView):
    model = Beer 
    
class BreweryListView(generic.ListView):
    model = Brewery    
    
class BreweryDetailView(generic.DetailView):
    model = Brewery     