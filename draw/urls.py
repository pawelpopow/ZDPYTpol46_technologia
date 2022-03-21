from django.urls import path
from intro import views

urlpatterns = [
    path('toto-lotek/', views.toto_lotek)
]