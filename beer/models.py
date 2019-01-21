from django.db import models
from datetime import date
from django.conf import settings
from django.urls import reverse
from django.utils import timezone 
from django.contrib.auth.models import User
from taggit.managers import TaggableManager
import numpy as np


class Beer(models.Model):
    name = models.CharField(max_length=100)
    brewery = models.CharField(max_length=100)
    country_of_origin = models.CharField(max_length=100)
    strength = models.DecimalField(max_digits=4, decimal_places=1)
    image = models.ImageField(blank=True, upload_to='images')
    tags = TaggableManager(blank=True, help_text='eg. IPA, Golden, Craft')
    added_by = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='beer_added_by',
                            on_delete=models.CASCADE) 
    added_date = models.DateTimeField(auto_now_add=True)
    likes = models.ManyToManyField(settings.AUTH_USER_MODEL, 
                                        related_name='likeds', blank=True)
   
   #https://stackoverflow.com/questions/11255243/how-to-get-average-across-different-models-in-django
    def average_rating(self):
        
        reviews = Review.objects.filter(beer=self)
        if reviews:
            count = len(reviews)
            sum = 0
            for rvw in reviews:
                sum += rvw.rating
            return round((sum/count),1)
        else:
            return 'No ratings yet'
            
    def total_likes(self):
        return self.likes.count()
    
    def save(self, *args, **kwargs):
        for field_name in ['name', 'brewery', 'country_of_origin']:
            val = getattr(self, field_name, False)
            if val:
                setattr(self, field_name, val.title())
        super(Beer, self).save(*args, **kwargs)        
        
        
    def get_absolute_url(self):
        """Returns the url to access a particular instance of a beer."""
        return reverse('beer-detail', args=[str(self.id)])
        
    def __str__(self):
        return self.name
        
    class Meta: 
        #order beers alphabetically, newest first
        ordering = ('name', '-added_date')     
        
class Review(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='beer_review',
                            on_delete=models.CASCADE) 
    beer = models.ForeignKey(Beer, 
                            on_delete=models.CASCADE,
                            related_name='reviews')
    created = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to='images', blank=True, null=True)
    notes = models.TextField(blank=True)
    RATING_CHOICES = ((1, 'one'), (2, 'two'), (3, 'three'), (4, 'four'), (5, 'five'))
    rating = models.PositiveSmallIntegerField('Rating (stars)', blank=False, default=3, choices=RATING_CHOICES)
    
    class Meta: 
        #order reviews alphabetically, newest first
        ordering = ('beer', '-created')  


    