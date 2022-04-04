from django.urls import reverse
from django.db import models


class Person(models.Model):
    name = models.CharField(max_length=64)
    age = models.IntegerField()
    city = models.CharField(max_length=64)

    def get_absolute_url(self):
        return reverse('viewapp:hello')
