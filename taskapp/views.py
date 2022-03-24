from django.shortcuts import render, redirect

# Pamięć ulotna RAM
# TASKS = []


def task_create_view(request):
    task = request.POST.get('task')

    if task:
        # Pamięć ulotna RAM
        # TASKS.append(task)

        # Pamięc trwała - plik
        with open('tasks.txt', 'a+') as f:
            f.write(f"{task}\n")

        return redirect('taskapp:task_list_view')

    return render(
        request,
        'taskapp/task-form.html',
    )


def task_list_view(request):
    # Pamięc trwała - plik
    with open('tasks.txt', 'r') as f:
        tasks = f.readlines()

    return render(
        request,
        'taskapp/task-list.html',
        context={
            'tasks': tasks,
        }
    )