from django.shortcuts import render
from django.shortcuts import HttpResponse


def hello(request):
    return HttpResponse("Hello, world")


def hey(request):
    return HttpResponse("czesc")
