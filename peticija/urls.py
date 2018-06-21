from django.urls import path

from . import views

app_name = "peticija"
urlpatterns = [
    path('', views.pocetna, name='pocetna'),
    path('<int:peticije_id>/', views.detalji, name='detalji'),
    path('spisak/', views.spisak, name="spisak"),
]
