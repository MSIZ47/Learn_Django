from django.shortcuts import render
from .models import *

def home(req):
    cheap = CheapPackage.objects.all()
    luxuray = LuxuryPackage.objects.all()
    camp = CampingPackage.objects.all()

    context = {'cheap':cheap,'luxuray':luxuray,'camp':camp}
    return render(req,"home/index.html",context=context)

def about(req):
    return render(req,"home/about.html")

def contact(req):
    return render(req,"home/contact.html")






    


