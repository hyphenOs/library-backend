# Copyright (c) 2020 hyphenOs Software Labs Private Limited

from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import generics
from .models import Book, Member
from .serializers import BookSerializer, MemberSerializer
from django_filters.rest_framework import DjangoFilterBackend


class BookList(generics.ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['title', 'author', 'year', 'isbn']


class BookDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer


class MemberList(generics.ListCreateAPIView):
    queryset = Member.objects.all()
    serializer_class = MemberSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['name', 'phone', 'email',
                        'address', 'city', 'state', 'zip_code']


class MemberDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Member.objects.all()
    serializer_class = MemberSerializer
