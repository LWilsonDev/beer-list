from django.urls import path

from . import views

urlpatterns = [
    path('donate', views.DonatePageView.as_view(), name='donate'),
    path('charge/', views.charge, name='charge'),
]