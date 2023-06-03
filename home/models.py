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
    
class NewsLetter(models.Model):
    email = models.EmailField()

    def __str__(self):
        return self.email


class ContactUs(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField()
    subject = models.CharField(max_length=200)
    message = models.TextField()

    def __str__(self):
        return self.name   






