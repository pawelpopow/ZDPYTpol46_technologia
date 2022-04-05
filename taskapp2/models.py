from django.urls import reverse
from django.db import models


class Task(models.Model):
    name = models.CharField(max_length=64)

    def get_absolute_url(self):
        return reverse("taskapp2:task-list")
