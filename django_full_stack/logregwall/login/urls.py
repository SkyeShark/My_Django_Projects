from django.urls import path     
from . import views
urlpatterns = [
    path('', views.index),
    path('register', views.register),
    path('success', views.success),
    path('login', views.login),
    path('logout', views.logout),
    path('message', views.post_message),
    path('comment_new/<int:id>', views.post_comment),	   
]