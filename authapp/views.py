from django.shortcuts import render, redirect
from django.shortcuts import HttpResponse
from django.views import View

from django.contrib.auth.models import User  # wbudowany w Django model użytkownika
from django.contrib.auth.forms import UserCreationForm  # wbudowany w Django formularz tworzenia użytkownika
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages


class UserCreateView(View):
    def get(self, request):
        form = UserCreationForm()
        return render(
            request,
            'authapp/user_form.html',
            context={
                'form': form,
            }
        )

    def post(self, request):
        form = UserCreationForm(request.POST)

        if form.is_valid():
            form.save()

        return redirect("authapp:user-create")


def cookies(request):
    # odczyt ciasteczek
    print(request.COOKIES)
    res = HttpResponse("OK")

    # zapis ciasteczek
    # res.set_cookie("ciasteczko1", 5)
    # res.set_cookie("ciasteczko2", 10, max_age=30)
    return res


def session(request):

    num_visit = request.session.get('num_visit', 0) + 1
    request.session['num_visit'] = num_visit

    return HttpResponse(f"Liczba odwiedzin: {num_visit}")


def msg(request):
    if request.method == "POST":
        task = request.POST.get("task")

        if task == "Pisanie":
            messages.error(request, "Wprowadziłeś niedozwoloną wartość.")
            return redirect('authapp:msg')

        return redirect('authapp:home')

    return render(
        request,
        'authapp/msg.html'
    )


def home(request):
    return render(
        request,
        'authapp/home.html',
    )


def login_view(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)  # uwierzytelnienie

        if user:
            login(request, user)

        return redirect('authapp:home')

    return render(
        request,
        'authapp/login.html',
    )


def logout_view(request):
    logout(request)
    return redirect('authapp:login')