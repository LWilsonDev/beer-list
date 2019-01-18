from django.shortcuts import render, get_object_or_404, redirect
from .models import Review, Beer, Beerlist
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib.auth.models import User
from django.urls import reverse, reverse_lazy
from django.views import generic
from .forms import BeerCreateForm, ReviewCreateForm
from django.contrib import messages
from taggit.models import Tag
from django.db.models import Avg


from django.core.files.storage import FileSystemStorage






def index(request):
    return render(request, 'index.html')
    
@login_required
def homepage(request):
    return render(request, 'beer/homepage.html')
    
def user_beer_list(request):
    
    user = request.user
    user_beers = Review.objects.filter(author=user)
    
    return render(request, 'beer/user_beers.html', {'user_beers':user_beers})
    
def beer_list(request, tag_slug=None):
    object_list = Beer.objects.all()
    object_list.annotate(
    avg_rating=Avg('reviews__rating'))
    
    tag = None
    
    if tag_slug:
        tag = get_object_or_404(Tag, slug=tag_slug)
        object_list = object_list.filter(tags__in=[tag])
        
    paginator = Paginator(object_list, 3) # 3 posts in each page
    page = request.GET.get('page')
    try:
        beers = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer deliver the first page
        beers = paginator.page(1)
    except EmptyPage:
        # If page is out of range deliver last page of results
        beers = paginator.page(paginator.num_pages)
       
       
   
    return render(request,
                  'beer/beer_list.html',
                  {'page': page,
                   'beers': beers,
                   'tag': tag
                       
                  })    
    
    #beers = Beer.objects.all().order_by('brewery', 'name')
    #return render(request, 'beer/all_beers.html', {'beers':beers})
    

    
#class BeerListView(generic.ListView):
 #  model = Beer
  
  
  
def beer_detail(request, pk):
    beer = get_object_or_404(Beer, pk=pk)
    reviews = beer.reviews.all()
    
    
    
    
    
    if request.method == "POST":
        form = ReviewCreateForm(request.POST, request.FILES)
        if form.is_valid():
            cd = form.cleaned_data
            new_item = form.save(commit=False)
            
            #assign user to item
            new_item.author = request.user
            new_item.beer = beer
            new_item.save()
            messages.success(request, 'Review added successfully')
            
    else:
        form = ReviewCreateForm()
    return render(request, 'beer/beer_detail.html', 
                    {'form':form, 'beer':beer, 'reviews': reviews})    



@login_required
def beer_create(request):
    if request.method == "POST":
        form = BeerCreateForm(request.POST, request.FILES)
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
                


