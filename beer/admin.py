from django.contrib import admin

from .models import Beer, Brewery, Review, Category

class ReviewAdmin(admin.ModelAdmin):
    model = Review
    list_display = ('beer', 'rating', 'author', 'created')
    list_filter = ['beer', 'author']
    search_fields = ['beer']

admin.site.register(Category)    
admin.site.register(Beer)
admin.site.register(Brewery)
admin.site.register(Review, ReviewAdmin)