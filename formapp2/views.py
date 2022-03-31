from django.shortcuts import render, redirect

from formapp2.models import Message
from formapp2.forms import ContactForm, MessageForm

def message_list(request):
    messages = Message.objects.all()

    return render(
        request,
        'formapp2/message_list.html',
        context={
            'messages': messages
        }
    )


# Formularz HTML
def contact1(request):
    if request.method == "POST":
        data = request.POST

        Message.objects.create(
            name=data.get('name'),
            email=data.get('email'),
            category=data.get('category'),
            subject=data.get('subject'),
            body=data.get('body')
        )

        return redirect('formapp2:message-list')

    return render(
        request,
        'formapp2/form1.html'
    )


# Formularz Django
def contact2(request):

    if request.method == "POST":
        form = ContactForm(request.POST)  # bound form

        if form.is_valid():
            data = form.cleaned_data

            Message.objects.create(
                name=data.get('name'),
                email=data.get('email'),
                category=data.get('category'),
                subject=data.get('subject'),
                body=data.get('body')
            )

        return redirect('formapp2:message-list')

    form = ContactForm()  # unbound form
    return render(
        request,
        'formapp2/form2.html',
        context={
            'form': form
        }
    )


# Formularz modelu
def contact3(request):

    if request.method == "POST":
        form = MessageForm(request.POST)  # bound form

        if form.is_valid():
            form.save()

        return redirect('formapp2:message-list')

    form = MessageForm()  # unbound form
    return render(
        request,
        'formapp2/form3.html',
        context={
            'form': form
        }
    )