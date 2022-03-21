from django.urls import  path

from newyear import views

urlpatterns = {
    path('/', views.new_year)
}