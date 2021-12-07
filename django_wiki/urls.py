from django.conf import settings
from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [

    path('', include('pages.urls')),
    path('admin/', admin.site.urls),
    path('accounts/', include('allauth.urls')),
    path('home/', views.home, name="home"),  
    path('djangowiki/', views.index, name="index"), 


]