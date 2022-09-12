from enum import unique
from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator
# Create your models here.

class Meal(models.Model):
    title = models.CharField(max_length=30)
    description = models.TextField(max_length=100)
    
    def no_of_ratings(self):
        rating = Rating.objects.filter(meal=self)
        return len(rating)


    def avg_rating(self):
        sum = 0
        ratings = Rating.objects.filter(meal=self)

        for x in ratings:
            sum += x.stars  

        if len(ratings) > 0:
            return sum / len(ratings)     
        else:  
            return 0

    def __str__(self):
        return self.title

class Drink(models.Model):
    title = models.CharField(max_length=30)
    description = models.TextField(max_length=100)

    def __str__(self):
        return self.title


class Rating(models.Model):
    meal = models.ForeignKey(Meal, on_delete=models.CASCADE, default=True)    
    drink = models.ForeignKey(Drink, on_delete=models.CASCADE, default=True)   
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    stars = models.IntegerField(validators=[MinValueValidator(1),MaxValueValidator(5)])
    

    class meta:
        unique_together =(('user', 'meal'),)
        index_together =(('user', 'meal'),)


