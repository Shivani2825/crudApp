
from django.urls import path
from . import views

urlpatterns = [
   path('',views.home),
   path('login',views.login),
   path('table',views.table),
   path('welcome',views.welcome),
   path('login',views.login),
   path('update',views.update),
     
]