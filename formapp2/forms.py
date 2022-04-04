from django import forms

from formapp2.models import Message


# formularz Django
class ContactForm(forms.Form):
    CHOICES = [
        ("q", "Pytanie"),
        ("o", "Inne")
    ]

    name = forms.CharField(label="Imię")
    email = forms.EmailField(label="Email")
    category = forms.ChoiceField(choices=CHOICES, label="Kategoria")
    subject = forms.CharField(required=False, label="Tytuł")
    body = forms.CharField(label="Treść", widget=forms.Textarea)


# formularz modelu
class MessageForm(forms.ModelForm):
    class Meta:
        model = Message
        fields = "__all__"
        labels = {
            "name": "Imię",
        }