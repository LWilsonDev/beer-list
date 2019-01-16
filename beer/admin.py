from django.contrib import admin

from .models import Beer, Beerlist, Review

class ReviewAdmin(admin.ModelAdmin):
    model = Review
    list_display = ('beer', 'rating', 'author', 'created')
    list_filter = ['beer', 'author']
    search_fields = ['beer']

    
admin.site.register(Beerlist)
admin.site.register(Beer)
admin.site.register(Review, ReviewAdmin)