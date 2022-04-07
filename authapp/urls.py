from django.urls import path

from authapp import views

app_name = 'authapp'

urlpatterns = [
    path('create/', views.UserCreateView.as_view(), name='user-create'),
    path('cookies/', views.cookies, name='cookies'),
    path('session/', views.session, name='session'),
    path('msg/', views.msg, name='msg'),
    path('home/', views.home, name='home'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
]