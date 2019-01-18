from django.shortcuts import render, get_object_or_404, redirect
from .models import Review, Beer
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib.auth.models import User
from django.urls import reverse, reverse_lazy
from django.views import generic
from .forms import BeerCreateForm, ReviewCreateForm
from django.contrib import messages
from taggit.models import Tag
from django.db.models import Avg
from django.http import JsonResponse
from django.views.decorators.http import require_POST
from django.core.files.storage import FileSystemStorage


def index(request):
    return render(request, 'index.html')
    
@login_required
def homepage(request):
    return render(request, 'beer/homepage.html')
    
def user_beer_list(request):
    
    user = request.user
    user_beers = Beerlist.objects.filter(user=user)
    
    return render(request, 'beer/user_beers.html', {'user_beers':user_beers})
    
def user_review_list(request):
    user = request.user
    user_reviews = Review.objects.filter(author=user)
    
    return render(request, 'beer/user_reviews.html', {'user_reviews':user_reviews})
    
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
                
@login_required
@require_POST
def beer_like(request):
    beer_id = request.POST.get('id')
    action = request.POST.get('action')
    if beer_id and action:
        try:
            beer = Beer.objects.get(id=beer_id)
            if action == 'like':
                beer.users_like.add(request.user)
            else:
                beer.users_like.remove(request.user)
            return JsonResponse({'status':'ok'})    
        except:
            pass
    return JsonResponse({'status':'ko'})    