from django.urls import path, include
from . import views
from django.conf.urls import url




urlpatterns = [
    path('', views.index, name='index'),
    path('beers/', views.beer_list, name='beer_list'),
    path('beers/tag/<slug:tag_slug>/', views.beer_list, name='beer_list_by_tag'),
    path('beer/<int:pk>', views.beer_detail, name='beer-detail'),
    path('add_beer/', views.beer_create, name='beer_create'),
    path('edit_beer/<int:pk>', views.beer_edit, name='beer_edit'),
    path('delete_beer/<int:pk>', views.beer_delete, name='beer_delete'),
    path('like', views.like_beer, name='like_beer'),
    path('users/<username>/', views.user_profile, name='user_profile'),
    
   
    
   
]
