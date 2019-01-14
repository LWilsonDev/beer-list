from django.shortcuts import render, get_object_or_404
from .models import Review, Beer, Brewery, Category 
from django.contrib.auth.models import User


def index(request):
    return render(request, 'index.html')
    
def user_beer_list(request):
    
    user = request.user
    user_beers = Review.objects.filter(author=user)
    
    return render(request, 'beer/user_beers.html', {'user_beers':user_beers})