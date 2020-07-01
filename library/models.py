# Copyright (c) 2020 hyphenOs Software Labs Private Limited

from django.db import models


class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    year = models.IntegerField()
    isbn = models.CharField(max_length=17, unique=True)

    class Meta:
        ordering = ['id']

    def __str__(self):
        return self.title


class Member(models.Model):
    name = models.CharField(max_length=100)
    phone = models.IntegerField()
    email = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    zip_code = models.IntegerField()

    class Meta:
        ordering = ['id']

    def __str__(self):
        return self.name
