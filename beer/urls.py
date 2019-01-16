from django.urls import path, include
from . import views
from django.conf.urls import url




urlpatterns = [
    path('', views.index, name='index'),
    path('homepage', views.homepage, name='homepage'),
    path('my_beers', views.user_beer_list, name='user_beer_list'),
    path('beers/', views.BeerListView.as_view(), name='beers'),
    path('beer/<int:pk>', views.beer_detail, name='beer-detail'),
    
    path('add_beer/', views.beer_create, name='beer_create'),
   
    
   
]
