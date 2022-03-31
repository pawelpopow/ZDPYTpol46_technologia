from django.urls import path

from taskapp import views

app_name = 'taskapp'

urlpatterns = [
    path('create/', views.task_create_view, name='task-create'),
    path('list/', views.task_list_view, name='task-list'),
    path('<int:pk>/', views.task_detail_view, name='task-detail'),
    path('update/<int:pk>/', views.task_update_view, name='task-update'),
    path('delete/<int:pk>/', views.task_delete_view, name='task-delete'),
]