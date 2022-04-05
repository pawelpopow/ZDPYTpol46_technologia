from django.urls import path

from authapp import views

app_name = 'authapp'

urlpatterns = [
    path('create/', views.UserCreateView.as_view(), name='user-create'),
]