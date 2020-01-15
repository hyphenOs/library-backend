from django.db import models

# Create your models here.


class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    year = models.IntegerField()
    isbn = models.CharField(max_length=17, unique=True)

    class Meta:
        ordering = ['id']

    def __str__(self):
        return self.title
