from django.shortcuts import render, get_object_or_404, redirect
from .models import Review, Beer, Brewery, Category
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.urls import reverse, reverse_lazy
from django.views import generic
from .forms import BeerCreateForm, BreweryCreateForm, BeerDetailForm, BreweryDetailForm, ReviewCreateForm
from django.contrib import messages

def index(request):
    return render(request, 'index.html')
    
@login_required
def homepage(request):
    return render(request, 'beer/homepage.html')
    
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
    


@login_required
def beer_create(request):
    if request.method == "POST":
        form = BeerCreateForm(data=request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            new_item = form.save(commit=False)
            
            #assign user to item
            new_item.added_by = request.user
            new_item.save()
            messages.success(request, 'Beer added successfully')
            #redirect to new item detail view
            return redirect(new_item.get_absolute_url())
    else:
        form = BeerCreateForm(data=request.GET)
    return render(request, 'beer/beer_form.html', 
                    {'form':form})    
                
@login_required
def brewery_create(request):
    if request.method == "POST":
        form = BreweryCreateForm(data=request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            new_item = form.save(commit=False)
            
            #assign user to item
            new_item.added_by = request.user
            new_item.save()
            messages.success(request, 'Brewery added successfully')
            #redirect to new item detail view
            return redirect(new_item.get_absolute_url())
    else:
        form = BreweryCreateForm(data=request.GET)
    return render(request, 'beer/brewery_form.html', 
                    {'form':form})   

