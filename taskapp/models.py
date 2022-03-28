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
    band = models.ForeignKey("Band", on_delete=models.CASCADE, null=True)


class Country(models.Model):
    name = models.CharField(max_length=64)
    capitol = models.OneToOneField('Capitol', on_delete=models.CASCADE)


class Capitol(models.Model):
    name = models.CharField(max_length=64)


class Framework(models.Model):
    name = models.CharField(max_length=64)
    language = models.ForeignKey('Language', on_delete=models.CASCADE)


class Language(models.Model):
    name = models.CharField(max_length=64)


class Character(models.Model):
    name = models.CharField(max_length=64)
    movies = models.ManyToManyField('Movie')


class Movie(models.Model):
    title = models.CharField(max_length=64)
