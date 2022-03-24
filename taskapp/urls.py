from django.urls import path

from taskapp import views

app_name = 'taskapp'

urlpatterns = [
    path('create/', views.task_create_view, name='task_create_view'),
    path('list/', views.task_list_view, name='task_list_view'),
]