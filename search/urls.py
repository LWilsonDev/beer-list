from django.urls import path, include
from . import views
from .views import search_beer

urlpatterns = [
     path('results/', views.search_beer, name='search_beer'),
]