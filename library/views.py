from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import generics
from .models import Book
from .serializers import BookSerializer
from django_filters.rest_framework import DjangoFilterBackend


class BookList(generics.ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['title', 'author', 'year', 'isbn']


class BookDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
