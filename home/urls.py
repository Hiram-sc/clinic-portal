from django.urls import path
from . import views 

urlpatterns = [
    path('', views.main_page, name='inicio'),
    path('sobre/', views.sobre, name='sobre'),
    path('blog/', views.blog, name='blog'),
    path('contato/', views.contato, name='contato'),
    path('agendar/', views.agendar_consulta, name='agendar_consulta')
]