from django.urls import path     
from . import views
urlpatterns = [
    path('', views.index),
    path('new', views.new),
    path('course/delete/<int:course_id>', views.delete),
    path('course/delete/confirm/<int:course_id>',views.destroy)	   
]