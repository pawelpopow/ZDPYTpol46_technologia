import datetime

from django.shortcuts import render


def new_year(request):
    now = datetime.datetime.now()

    if now.day == 1 and now.month == 1:
        is_it_new_year = True
    else:
        is_it_new_year = False

    return render(
        request,
        'newyear/new-year.html',
        context={
            ' is_it_new_year ':  is_it_new_year,
        }
    )
