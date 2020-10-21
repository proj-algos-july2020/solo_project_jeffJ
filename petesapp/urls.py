from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('classes', views.classes),
    path('appointment', views.appointment)

    # path('login', views.login),
    # path('registration', views.registration),
    # path('reg', views.regPost),
    # path('user', views.userPage),
    # path('comments', views.comments),
    # path('logout', views.logout),
    # path('chat', views.chat),
    # path('delete_comment/<int:comments_id>', views.deleteComment),
    # path('video', views.videos)

]
