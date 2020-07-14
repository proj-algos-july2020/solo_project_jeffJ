from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('login', views.login),
    path('registration', views.registration),
    path('reg', views.reg),
    path('user', views.user),
    path('comments', views.comments),
    path('logout', views.logout),

]
