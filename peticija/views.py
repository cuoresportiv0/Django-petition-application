from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.shortcuts import render

from peticija.models import Peticije


def pocetna(request):
        lista=Peticije.objects.all()

        context = {
                'lista': lista,
        }
        return render(request , "peticija/pocetna.html" , context)


def detalji(request, peticije_id):
    peticij = get_object_or_404(Peticije, pk=peticije_id)
    return render(request, 'peticija/detalji.html', {'peticij': peticij})