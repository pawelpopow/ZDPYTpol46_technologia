from django.shortcuts import render, redirect

from taskapp.models import Task

# Pamięć ulotna RAM
# TASKS = []


def task_create_view(request):
    task = request.POST.get('task')

    if task:
        # Pamięć ulotna RAM
        # TASKS.append(task)

        # # Pamięc trwała - plik
        # with open('tasks.txt', 'a+') as f:
        #     f.write(f"{task}\n")

        Task.objects.create(name=task)

        return redirect('taskapp:task-list')

    return render(
        request,
        'taskapp/task_form.html',
    )


def task_list_view(request):
    # # Pamięc trwała - plik
    # with open('tasks.txt', 'r') as f:
    #     tasks = f.readlines()

    # Pamięć trwała - baza
    tasks = Task.objects.all()

    return render(
        request,
        'taskapp/task_list.html',
        context={
            'tasks': tasks,
        }
    )


def task_detail_view(request, pk):
    task = Task.objects.get(pk=pk)

    return render(
        request,
        'taskapp/task_detail.html',
        context={
            'task': task,
        }
    )