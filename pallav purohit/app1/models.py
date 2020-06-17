
from django.db import models
# Create your models here.

class Employee(models.Model):
        first_name = models.CharField(max_length=220)
        last_name = models.CharField(max_length=220)
        start_date = models.DateField(null=True)
        def __str__(self):
                return str(self.first_name)

class image(models.Model):
        title = models.TextField(null=True)
        cover = models.ImageField(upload_to ='images/')
        def __str__(self):
                return str(self.title)



class Zomato(models.Model):
        Restaurant = models.CharField(max_length=250)
        City = models.CharField(max_length=250)
        Cuisines = models.CharField(max_length=250)
        cost = models.IntegerField(null=True)
        tablebook = models.CharField(max_length=250)
        onlinedelivery = models.CharField(max_length=250)
        rating = models.IntegerField(null=True)
        Votes = models.IntegerField(null=True)
        def __str__(self):
                return str(self.City)
  


class zoamto(models.Model):
        Restaurant = models.CharField(max_length=250)
        PRICE = models.IntegerField(null=True)
        CUISINECATEGORY = models.CharField(max_length=250)
        CITY = models.CharField(max_length=250)
        REGION = models.CharField(max_length=250, null=True)
        CUISINETYPE = models.CharField(max_length=250)
       
        RATING = models.IntegerField(null=True)
        RATING_TYPE = models.CharField(max_length=250)
        
