from django.urls import path
from . import views 

from .seo import robots_txt
from django.contrib.sitemaps.views import sitemap
from home.sitemap import StaticViewSitemap

sitemaps = {
    'static': StaticViewSitemap,
}

urlpatterns = [
    path('', views.home, name='home'),
    path('para_pais/', views.para_pais, name='para_pais'),
    path('agendar/', views.agendar, name='agendar_consulta'),
    
    path('robots.txt', robots_txt, name='robots_txt'),
    path('sitemap.xml', sitemap, {'sitemaps': sitemaps}, name='sitemap'),
]