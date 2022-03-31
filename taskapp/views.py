from django.shortcuts import render, redirect, get_object_or_404

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
    # from django.core.exceptions import ObjectDoesNotExist
    # from django.http import Http404
    # try:
    #     task = Task.objects.get(pk=pk)
    # except ObjectDoesNotExist:
    #     raise Http404

    task = get_object_or_404(Task, pk=pk)

    return render(
        request,
        'taskapp/task_detail.html',
        context={
            'task': task,
        }
    )


def task_update_view(request, pk):
    task = get_object_or_404(Task, pk=pk)

    modified_task = request.POST.get("task")
    if modified_task:
        task.name = modified_task
        task.save()

        return redirect('taskapp:task-list')

    return render(
        request,
        'taskapp/task_form.html',
        context={
            'task': task,
        }
    )


def task_delete_view(request, pk):
    task = get_object_or_404(Task, pk=pk)

    if request.method == "POST":
        task.delete()
        return redirect('taskapp:task-list')

    return render(
        request,
        'taskapp/task_confirm_delete.html',
        context={
            'task': task,
        }
    )