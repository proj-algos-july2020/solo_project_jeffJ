from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('login', views.login),
    path('registration', views.registration),
    path('reg', views.regPost),
    path('user', views.userPage),
    path('comments', views.comments),
    path('logout', views.logout),
    # path('edit_comment/<int:comments_id>', views.commentEdit),
    path('delete_comment/<int:comments_id>', views.deleteComment),
    path('video', views.videos)

]
