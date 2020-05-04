from django.urls import path     
from . import views
urlpatterns = [
    path('', views.index),
    path('books',views.books),
    path('register',views.register),
    path('login',views.login),
    path('logout',views.logout),
    path('myaccount/logout', views.logout),
    path('myaccount/<int:user_id>',views.edit),
    path('myaccount/update/<int:user_id>',views.update),
    path('postbook', views.postbook),
    path('like/<int:book_id>',views.liking),
    path('unlike/<int:book_id>',views.unlike),
    path('book/<int:book_id>', views.bookpage),
    path('delete/<int:book_id>/<int:user_id>', views.delete),
    path('update/<int:book_id>', views.update),
    path('book/update/<int:book_id>', views.update)	   	   
]