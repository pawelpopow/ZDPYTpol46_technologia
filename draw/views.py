import random

from django.shortcuts import render


def toto_lotek(request):

    res = random.sample(range(1, 49), 6)

    return render(
        request,
        'draw/toto_lotek.html',
        context={
            'res': res,
        }
    )
