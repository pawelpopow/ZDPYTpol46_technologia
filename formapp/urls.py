from django.urls import path

from formapp import views

app_name = 'formapp'

urlpatterns = [
    path('name-get/', views.name_get, name='name_get'),
    path('name-post/', views.name_post, name='name_post'),
    path('hello/<str:name>/', views.hello, name='hello'),
]
