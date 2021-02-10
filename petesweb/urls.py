from django.urls import path, include 
from django.contrib import admin
from django.views.generic import TemplateView

urlpatterns = [
    path('', include('petesapp.urls')),
    path('admin/', admin.site.urls),
    path('accounts/', include('allauth.urls')),
    
]
