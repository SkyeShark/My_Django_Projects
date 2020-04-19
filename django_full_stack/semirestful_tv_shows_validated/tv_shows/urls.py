from django.urls import path     
from . import views
urlpatterns = [
    path('', views.index),
    path('shows', views.shows),
    path('shows/<int:show_id>',views.displayshow),
    path('shows/<int:show_id>/edit',views.editshow),
    path('shows/<int:show_id>/update',views.update),
    path('shows/new',views.new),
    path('shows/create',views.create),
    path('shows/<int:show_id>/destroy',views.destroy)
]