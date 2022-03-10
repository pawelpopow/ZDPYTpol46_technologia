from django.urls import path
from intro import views


urlpatterns = [
    path('home/', views.hello),
    path('home2/', views.hello2),
    path('home3/', views.hello3),
    path('next/', views.hey),
    path('adam/', views.adam),
    path('ewa/', views.ewa),
    path('hello/thought/', views.hello_app),
    path('<str:name>/', views.name_view),
]