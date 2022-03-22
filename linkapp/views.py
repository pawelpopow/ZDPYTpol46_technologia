from django.shortcuts import render


def first(request):
    return render(
        request,
        'linkapp/first.html',
    )


def second(request):
    return render(
        request,
        'linkapp/second.html',
    )


def third(request, param):
    return render(
        request,
        'linkapp/third.html',
        context={
            'param': param,
        }
    )
