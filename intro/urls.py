from django.urls import path
from intro import views


urlpatterns = [
    path('home/', views.hello),
    path('next/', views.hey)
]