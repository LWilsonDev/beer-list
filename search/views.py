from django.shortcuts import render
from beer.models import Beer
from django.db.models import Q
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

#https://docs.djangoproject.com/en/dev/topics/db/queries/#complex-lookups-with-q-objects
def search_beer(request):
    query = request.GET.get('q')
    if query:
        # Use Django Q object to chain queries, searching for matches in beer name, location, and brewery
        results = Beer.objects.filter(Q(name__icontains=query) | Q(brewery__icontains=query) | Q(country_of_origin__icontains=query))
        object_list = results
        paginator = Paginator(object_list, 4) # 8 beers in each page
        page = request.GET.get('page')
        try:
            beers = paginator.page(page)
        except PageNotAnInteger:
            # If page is not an integer deliver the first page
            beers = paginator.page(1)
        except EmptyPage:
            # If page is out of range deliver last page of results
            beers = paginator.page(paginator.num_pages)
    else:
        return "No results"
    
    return render(request, "beer/search_results.html", {'results':results,'beers': beers, 'page':page, 'query': query})    
    
    