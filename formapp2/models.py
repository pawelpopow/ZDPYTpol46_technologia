from django.db import models


class Message(models.Model):
    
    CHOICES = [
        ("q", "Pytanie"),
        ("o", "Inne")
    ]

    name = models.CharField(max_length=128)
    email = models.EmailField()
    category = models.CharField(max_length=10)
    subject = models.CharField(max_length=100)
    body = models.TextField()
    added = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
