from django.db import models



#django-data-type
#geeksforgeeks

class CheapPackage(models.Model):
    city = models.CharField(max_length=50)
    price = models.IntegerField()

    def __str__(self):
        return self.city

class LuxuryPackage(models.Model):
    city = models.CharField(max_length=50)
    price = models.IntegerField()

    def __str__(self):
        return self.city

class CampingPackage(models.Model):
    city = models.CharField(max_length=50)
    price = models.IntegerField()

    def __str__(self):
        return self.city







