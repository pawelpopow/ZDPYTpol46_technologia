from django.urls import path

from formapp import views

app_name = 'formapp'

urlpatterns = {
    path('name-get/', views.name_get, name='name_get'),
}
