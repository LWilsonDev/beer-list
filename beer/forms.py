from django import forms
from .models import Brewery, Beer, Review, Category

# add beer and brewery forms seperated into basic and detailed forms for better UX. 
# Users can add just brewery and beer names and add extra info at a later date, or leave to another user

class BreweryCreateForm(forms.ModelForm):
    """Form to add bare minimum brewery info"""
    class Meta:
        model = Brewery
        fields = ('name',)
        widgets = {
            'text': forms.TextInput(attrs={
                'id': 'post-text', 
                'required': True, 
                'placeholder': 'Say something...'
            })
            }

class BreweryDetailForm(forms.ModelForm):
    """Form to add detailed brewery info"""
    class Meta:
        model = Brewery
        fields = ('name', 'country', 'region', 'town', 'image', 'founded_year')
        
class BeerCreateForm(forms.ModelForm):
    """Form to add bare minimum beer info"""
    class Meta:
        model = Beer
        fields = ('brewery', 'name', 'tags')
        
class BeerDetailForm(forms.ModelForm):
    """Form to add detailed beer info"""
    class Meta:
        model = Beer
        fields = ('brewery', 'category', 'name', 'strength', 'image', 'tags')
        
class ReviewCreateForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ('image', 'notes', 'rating')