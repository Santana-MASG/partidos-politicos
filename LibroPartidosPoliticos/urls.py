from django.urls import path
from LibroPartidosPoliticos import views

app_name = 'partidos'

urlpatterns=[
    path('home/',views.home, name='home')
]