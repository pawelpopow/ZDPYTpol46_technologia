import datetime

from django.shortcuts import render


def new_year(request):
    now = datetime.datetime.now()
