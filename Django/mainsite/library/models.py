from django.db import models
import datetime
from django.utils import timezone, dateformat


class Author (models.Model):
    firstName = models.CharField(max_length=50)
    lastName = models.CharField(max_length=50)

    def __str__(self):
        return f'{self.firstName} {self.lastName}'


class Book (models.Model):
    title = models.CharField(max_length=100)
    pubDate = models.DateField()
    author = models.ForeignKey(Author)   # foreign key
    checked_in = models.BooleanField(default=True)
    user = models.CharField(max_length=100, null=True)
    timestamp = models.DateField(default=timezone.now)


    def __str__(self):
        return f'{self.title}'


class RentalStatus(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    checked_in = models.BooleanField()
    user = models.CharField(max_length=100, null=True)
    timestamp = models.DateField(default=timezone.now)

