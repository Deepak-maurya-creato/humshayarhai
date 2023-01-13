
from django.urls import path,include
from django.conf.urls.static import static
from django.conf import settings
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('home/', views.home, name='home'),
    path('love/', views.love, name='love'),
    path('dosti/', views.dosti, name='dosti'),
    path('wish/', views.wish, name='wish'),
    path('contact/', views.contact, name='contact'),
    path('sad/', views.sad, name='sad'),
    path('dhokha/', views.dhokha, name='dhokha'),
    path('alone/', views.alone, name='alone'),
    path('break_up/', views.break_up, name='break-up'),
    path('bhakti/', views.bhakti, name='bhakti'),
    path('deshbhakti/', views.deshbhakti, name='deshbhakti'),
    path('thought/', views.thought, name='thought'),
    
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)