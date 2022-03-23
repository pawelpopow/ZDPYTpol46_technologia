from django.shortcuts import render, redirect


def name_get(request):
    name = request.GET.get('name')

    if name:
        return render(
            request,
            'formapp/hello.html',
            context={
                'name': name,
            }
        )

    return render(
        request,
        'formapp/name_get.html',
    )


def name_post(request):
    name = request.POST.get('name')

    if name:
        return redirect('formapp:hello', name=name)

    return render(
        request,
        'formapp/name_post.html',
    )


def hello(request, name):
    return render(
        request,
        'formapp/hello.html',
        context={
            'name': name,
        }
    )