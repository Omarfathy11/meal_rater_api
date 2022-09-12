from django.contrib import admin
from . models import Drink, Meal, Rating
# Register your models here.


class RatingAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'meal', 'stars']
    list_filter = ['user', 'meal']



class MealAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'description']
    search_fields = ['title', 'description']
    list_filter = ['title', 'description']

class DrinkAdmin(admin.ModelAdmin):
     list_display = ['id', 'title', 'description']
     search_fields = ['title', 'description']
     list_filter = ['title', 'description']



admin.site.register(Meal, MealAdmin)
admin.site.register(Rating, RatingAdmin)
admin.site.register(Drink, DrinkAdmin)

 