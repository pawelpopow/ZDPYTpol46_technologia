from django.shortcuts import render
from django.shortcuts import HttpResponse


def hello(request):
    return HttpResponse("Hello, world")


def hey(request):
    return HttpResponse("czesc")


def adam(request):
    return HttpResponse("Cześć, Adam!")


def ewa(request):
    return HttpResponse("Cześć, Ewa!")


def name_view(request, name):
    msg = f"Cześć, {name.title()}!"
    return HttpResponse(msg)


def hello_app(request):
    return HttpResponse("Wszystko gra!")


def hello2(request):
    content = "<!DOCUMENT html><html><head><body><h1> Witaj, świecie>"
    return HttpResponse(content)


def hello3(request):
    return render(
        request,
        'hello.html'
    )
