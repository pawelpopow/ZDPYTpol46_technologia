from django.shortcuts import render, redirect
from django.views import View

from django.contrib.auth.models import User  # wbudowany w Django model użytkownika
from django.contrib.auth.forms import UserCreationForm  # wbudowany w Django formularz tworzenia użytkownika


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
