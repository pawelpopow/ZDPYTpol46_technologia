from django.shortcuts import render


def name(request):

    print(request.GET)

    return render(
        request,
        'formapp/name.html',
    )
