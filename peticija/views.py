from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render

from peticija.models import Peticije


def pocetna(request):
        lista=Peticije.objects

        context = {
                'lista': lista,
        }
        return render(request , "peticija/pocetna.html" , context)