from django.urls import path

from . import views


app_name = 'calculator'
urlpatterns = [path('add/', views.add, name='add')]