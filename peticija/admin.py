from django.contrib import admin

from django.contrib import admin

from .models import Peticije,Potpisanti,Potpisane

admin.site.register(Peticije)
admin.site.register(Potpisanti)
admin.site.register(Potpisane)
