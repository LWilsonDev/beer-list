from django.urls import path, include
from . import views
from django.conf.urls import url




urlpatterns = [
    path('', views.index, name='index'),
    path('my_beers', views.user_beer_list, name='user_beer_list'),
   #path('all_beers', views.all_beers, name='all_beers'),
   #path('breweries', views.breweries, name='breweries'),
   #path('brewery_detail', views.brewery_detail, name="brewery_detail"),
    path('beers/', views.BeerListView.as_view(), name='beers'),
    path('beer/<int:pk>', views.BeerDetailView.as_view(), name='beer-detail'),
    path('breweries/', views.BreweryListView.as_view(), name='breweries'),
    path('brewery/<int:pk>', views.BreweryDetailView.as_view(), name='brewery-detail')
   
]