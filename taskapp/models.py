from django.db import models


class Task(models.Model):
    name = models.CharField(max_length=64)


class Band(models.Model):
    name = models.CharField(max_length=64)
    year = models.IntegerField()
    still_active = models.BooleanField(default=True)


class Category(models.Model):
    name = models.CharField(max_length=64)
    description = models.TextField(null=True)


class Article(models.Model):
    title = models.CharField(max_length=128)
    author = models.CharField(max_length=64, null=True)
    content = models.TextField(null=True)
    data_added = models.DateTimeField(auto_now_add=True)


class Album(models.Model):
    title = models.CharField(max_length=128)
    year = models.IntegerField()
    rating = models.DecimalField(max_digits=3, decimal_places=1)
