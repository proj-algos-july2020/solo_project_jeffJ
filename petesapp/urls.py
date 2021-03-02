from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('classes', views.classes),
    path('gym', views.gym),
    path('regForm', views.regForm),
    path('login', views.login),
    path('about', views.about),
    path("schedule", views.schedule),
    path('comments', views.comments),
    path('contact', views.contact),
    path('question', views.question)

]
