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
    # path('registration', views.registration),
    # path('reg', views.regPost),
    # path('logout', views.logout),
    # path('chat', views.chat),
    # path('delete_comment/<int:comments_id>', views.deleteComment),
    # path('video', views.videos)

]
