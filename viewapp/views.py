from django.shortcuts import render, HttpResponse
from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse_lazy
from django import views

from django.views.generic import TemplateView
from django.views.generic import DetailView
from django.views.generic import CreateView

from viewapp.models import Person
from viewapp.forms import PersonForm


# function-based view
def hello(request):
    return HttpResponse("Hello, world!")


# class-based view
class HelloView(views.View):
    def get(self, request):
        return HttpResponse("Hello, world!")


# A szablony ?
# function-based view
def hello_template(request):
    return render(
        request,
        'viewapp/hello.html'
    )


# class-based view
class HelloClassView(views.View):
    def get(self, request):
        return render(
            request,
            'viewapp/hello.html'
        )


# generic view
class HelloTemplateView(TemplateView):
    template_name = 'viewapp/hello.html'


# function-based view
def hello_template2(request):
    name = "Jan"
    return render(
        request,
        'viewapp/hello2.html',
        context={
            "name": name,
        }
    )


# class-based view
class HelloClassView2(views.View):
    def get(self, request):
        name = "Jan"
        return render(
            request,
            'viewapp/hello2.html',
            context={
                "name": name
            }
        )


# generic view
class HelloTemplateView2(TemplateView):
    template_name = 'viewapp/hello2.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["name"] = "Jan"
        return context


# A modele ? CRUD
# 1. Literka R - detal

# function-based view
def person_detail(request, id):
    p = get_object_or_404(Person, id=id)
    return render(
        request,
        'viewapp/person_detail.html',
        context={
            'person': p
        }
    )


# class-based view
class PersonView(views.View):
    def get(self, request, id):
        p = get_object_or_404(Person, id=id)
        return render(
            request,
            'viewapp/person_detail.html',
            context={
                'person': p,
            }
        )


# generic view
class PersonDetailView(DetailView):
    model = Person


# 2. Literka C

# function-based view
def create_person(request):
    if request.method == "POST":
        form = PersonForm(request.POST)

        if form.is_valid():
            form.save()

        return redirect('viewapp:hello')

    form = PersonForm()
    return render(
        request,
        'viewapp/person_form.html',
        context={
            'form': form,
        }
    )


# class-based view
class PersonCreateView(views.View):
    def get(self, request):
        form = PersonForm()
        return render(
            request,
            'viewapp/person_form.html',
            context={
                'form': form,
            }
        )

    def post(self, request):
        form = PersonForm(request.POST)

        if form.is_valid():
            form.save()

        return redirect('viewapp:hello')


# generic view
class PersonCreateView2(CreateView):
    model = Person
    fields = '__all__'
    # success_url = reverse_lazy('viewapp:hello')
