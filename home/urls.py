from django.urls import path
from . import views 

urlpatterns = [
    path('', views.home, name='home'),
    path('para_pais/', views.para_pais, name='para_pais'),
    path('agendar/', views.agendar, name='agendar_consulta')
]