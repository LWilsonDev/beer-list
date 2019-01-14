from django.db import models
from datetime import date
from django.utils import timezone 
from django.contrib.auth.models import User
from taggit.managers import TaggableManager
import numpy as np





class Brewery(models.Model):
    name = models.CharField(max_length=100)
    country = models.CharField(max_length=50)
    town = models.CharField(max_length=50)
    image = models.ImageField(upload_to='images', blank=True, null=True)
    
    def __str__(self):
        return self.name
        
class Beer(models.Model):
    brewery = models.ForeignKey(Brewery, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='images', blank=True, null=True)
    tags = TaggableManager()
    # https://www.codementor.io/jadianes/get-started-with-django-building-recommendation-review-app-du107yb1a
    def average_rating(self):
        all_ratings = map(lambda x: x.rating, self.review_set.all())
        return np.mean(all_ratings)
    
    def __str__(self):
        return self.name
        
class Review(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='beer_review'
                            on_delete=models.CASCADE) 
    beer = models.ForeignKey(Beer, 
                            on_delete=models.CASCADE,
                            related_name='reviews')
    created = models.DateTimeField(auto_now_add=True)                         
    notes = models.TextField(blank=True)
    RATING_CHOICES = ((1, 'one'), (2, 'two'), (3, 'three'), (4, 'four'), (5, 'five'))
    rating = models.PositiveSmallIntegerField('Rating (stars)', blank=False, default=3, choices=RATING_CHOICES)
    
    class Meta: 
        #order reviews alphabetically
        ordering = ('beer')  

 
    