from django.urls import path, include
from . import views
from django.conf.urls import url




urlpatterns = [
    path('', views.index, name='index'),
    path('homepage', views.homepage, name='homepage'),
    path('my_beers', views.user_beer_list, name='user_beer_list'),
    path('beers/', views.BeerListView.as_view(), name='beers'),
    path('beer/<int:pk>', views.BeerDetailView.as_view(), name='beer-detail'),
    path('breweries/', views.BreweryListView.as_view(), name='breweries'),
    path('brewery/<int:pk>', views.BreweryDetailView.as_view(), name='brewery-detail'),
    path('add_beer/', views.beer_create, name='beer_create'),
    path('add_brewery/', views.brewery_create, name='brewery_create'),
    
   
]