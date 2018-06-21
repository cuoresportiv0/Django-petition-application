from django.db import models
from django.forms import ModelForm

# Create your models here.
class Peticije(models.Model):
    naziv = models.CharField(max_length=1000)
    text_peticije = models.TextField()
    datum_pocetka = models.DateField()
    datum_zavrsetka = models.DateField()
    broj_potpisa= models.IntegerField()

    def __str__(self):
        return self.naziv


class Potpisanti(models.Model):
    ime = models.CharField(max_length=100)
    prezime = models.CharField(max_length=100)
    prebivaliste = models.CharField(max_length=50)
    jmbg = models.CharField(max_length=40)

    def __str__(self):
        return self.jmbg


class Potpisane(models.Model):
    id_peticije = models.ForeignKey(Peticije, unique=False, on_delete=models.CASCADE)
    id_potpisanta = models.ForeignKey(Potpisanti, unique=False, on_delete=models.CASCADE)


    class Meta:
        unique_together = ('id_peticije', 'id_potpisanta')


class PotpisantiForm(ModelForm):
    class Meta:
        model = Potpisanti
        fields = ['ime', 'prezime', 'prebivaliste', 'jmbg']
        labels = {
            'ime': ('Unesite ime:'),
            'prezime': ('Unesite prezime:'),
            'prebivaliste': ('Vase prebivaliste:'),
            'jmbg': ('Unesite jmbg:')
        }
