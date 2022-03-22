from django.shortcuts import render


def mem(request):
    return render(
        request,
        'mem/sample.html',
    )

