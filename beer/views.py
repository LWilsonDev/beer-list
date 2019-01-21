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
from django.http import JsonResponse, HttpResponse, HttpResponseRedirect
from django.views.decorators.http import require_POST
from django.core.files.storage import FileSystemStorage
from django.db.models import Count
from django.views.generic import UpdateView
from django.template.loader import render_to_string


def index(request):
    recent_beers = Beer.objects.order_by('-added_date')[:4]
    
    return render(request, 'index.html', {'recent_beers':recent_beers})
    
    

def user_review_list(request):
    user = request.user
    beer_user_has_reviewed = Beer.objects.filter(reviews__author=user)
    
    return render(request, 'beer/user_reviews.html', {'user_reviews':beer_user_has_reviewed})
    
def beer_list(request, tag_slug=None):
    object_list = Beer.objects.all()
    
    tag = None
    
    if tag_slug:
        tag = get_object_or_404(Tag, slug=tag_slug)
        object_list = object_list.filter(tags__in=[tag])
        
    paginator = Paginator(object_list, 4) # 4 posts in each page
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
    is_liked = False
    if beer.likes.filter(id=request.user.id).exists():
        is_liked=True
    review_list = beer.reviews.all()
    
    paginator = Paginator(review_list, 4) # 4 reviews each page
    page = request.GET.get('page')
    try:
        reviews = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer deliver the first page
        reviews = paginator.page(1)
    except EmptyPage:
        # If page is out of range deliver last page of results
        reviews = paginator.page(paginator.num_pages)
      
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
        
    # get similar beers 
    beer_tags_ids = beer.tags.values_list('id', flat=True)
    similar_beers = Beer.objects.filter(tags__in=beer_tags_ids).exclude(id=beer.id)
    similar_beers = similar_beers.annotate(same_tags=Count('tags')).order_by('-same_tags', '-added_date')[:3]
    context = {
        'form':form, 
        'beer':beer, 
        'reviews': reviews, 
        'page':page, 
        'similar_beers': similar_beers,
        'is_liked':is_liked,
    
    }
    return render(request, 'beer/beer_detail.html', 
                    context)    


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
        form = BeerCreateForm()
    return render(request, 'beer/beer_form.html', 
                    {'form':form})    
   
@login_required
def beer_edit(request, pk):
    beer = get_object_or_404(Beer, pk=pk)
    if request.method == 'POST':
        form = BeerCreateForm(request.POST, instance=beer)
        try:
            if form.is_valid():
                form.save()
                messages.success(request, 'Beer succesfully updated')
                return redirect(beer.get_absolute_url())
        except Exception as e:
            messages.warning(request, 'There was an issue saving your updates {}'.format(e))
    else:
        form = BeerCreateForm(instance=beer)
    return render(request, 'beer/beer_form.html', {'form':form, 'beer':beer})    

@login_required   
def like_beer(request):
    #beer = get_object_or_404(Beer, id=request.POST.get('beer_id'))
    beer = get_object_or_404(Beer, id=request.POST.get('id'))
    is_liked = False
    if beer.likes.filter(id=request.user.id).exists():
        beer.likes.remove(request.user)
        is_liked = False
    else:    
        beer.likes.add(request.user)
        is_liked = True
    context = {
        'beer':beer,
        'is_liked':is_liked,
    }
    if request.is_ajax():
        #django recommends using render_to_string to cut down repetative loading and rendering of templates
        html = render_to_string('beer/like_section.html', context, request=request)
        return JsonResponse({'form':html})
    