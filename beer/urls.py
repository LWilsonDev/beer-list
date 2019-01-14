from django.urls import path, include
from . import views
from django.conf.urls import url




urlpatterns = [
    path('', views.index, name='index'),
    path('my_beers', views.user_beer_list, name='user_beer_list')
]