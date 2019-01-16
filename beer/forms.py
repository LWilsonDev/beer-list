from django import forms
from .models import  Beer, Review

# add beer and brewery forms seperated into basic and detailed forms for better UX. 
# Users can add just brewery and beer names and add extra info at a later date, or leave to another user




        
class BeerCreateForm(forms.ModelForm):
    """Form to add bare minimum beer info"""
    class Meta:
        model = Beer
        fields = ('name', 'brewery', 'country_of_origin', 'strength', 'image', 'tags')
        

        
class ReviewCreateForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ('image', 'notes', 'rating')