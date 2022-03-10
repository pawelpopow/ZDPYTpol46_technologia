from django.urls import path
from intro import views


urlpatterns = [
    path('home/', views.hello),
    path('next/', views.hey),
    path('adam/', views.adam),
    path('ewa/', views.ewa),
    path('<str:name>/', views.name_view),
]