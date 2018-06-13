from django.db import models


# Create your models here.
class Peticije(models.Model):
    naziv = models.CharField
    text_peticije = models.TextField
    datum_pocetka = models.DateField
    datum_zavrsetka = models.DateField

    def __self__(self):
        return self.naziv


class Potpisanti(models.Model):
    ime = models.CharField
    prezime = models.CharField
    prebivaliste = models.CharField
    jmbg = models.CharField


class Potpisane(models.Model):
    id_peticije = models.ForeignKey(Peticije, unique=False, on_delete=models.CASCADE)
    id_potpisanta = models.ForeignKey(Potpisanti, unique=False, on_delete=models.CASCADE)
    komentar = models.TextField

    class Meta:
        unique_together = ('id_peticije', 'id_potpisanta')
