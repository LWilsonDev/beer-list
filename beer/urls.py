from django.urls import path, include
from . import views
from django.conf.urls import url




urlpatterns = [
    path('', views.index, name='index'),
    path('homepage', views.homepage, name='homepage'),
    path('my_beers', views.user_beer_list, name='user_beer_list'),
    path('my_reviews', views.user_review_list, name='user_review_list'),
    path('beers/', views.beer_list, name='beer_list'),
    path('beers/tag/<slug:tag_slug>/', views.beer_list, name='beer_list_by_tag'),
    path('beer/<int:pk>', views.beer_detail, name='beer-detail'),
    path('add_beer/', views.beer_create, name='beer_create'),
    path('like/', views.beer_like, name='like'),
   
    
   
]
