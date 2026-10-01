from django.contrib import admin

# Register your models here.
from .models import Movie, Review

class MovieAdmin(admin.ModelAdmin):
    ordering = ['name']
    search_fields = ['name']

class ReviewAdmin(admin.ModelAdmin):
    list_display = ['user', 'movie', 'comment', 'reported']
    list_filter = ['reported']

admin.site.register(Movie, MovieAdmin)
admin.site.register(Review, ReviewAdmin)