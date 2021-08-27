from django.db import models

# Create your models here.

class Country(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class State(models.Model):
    country = models.ForeignKey(Country,on_delete=models.CASCADE)
    state = models.CharField(max_length=50)

    def __str__(self):
        return self.state

class City(models.Model):
    state = models.ForeignKey(State,on_delete=models.CASCADE)
    city = models.CharField(max_length=50)

    def __str__(self):
        return self.city

        
        


