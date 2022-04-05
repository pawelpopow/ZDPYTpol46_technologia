from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView
from django.views.generic import CreateView, UpdateView, DeleteView

from taskapp2.models import Task


class TaskListView(ListView):
    model = Task


class TaskDetailView(DetailView):
    model = Task


class TaskCreateView(CreateView):
    model = Task
    fields = "__all__"


class TaskUpdateView(UpdateView):
    model = Task
    fields = "__all__"


class TaskDeleteView(DeleteView):
    model = Task
    success_url = reverse_lazy('taskapp2:task-list')
