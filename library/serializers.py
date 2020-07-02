# Copyright (c) 2020 hyphenOs Software Labs Private Limited

from rest_framework import serializers
from .models import Book, Member


class BookSerializer(serializers.ModelSerializer):

    class Meta:
        model = Book
        fields = '__all__'


class MemberSerializer(serializers.ModelSerializer):

    class Meta:
        model = Member
        fields = '__all__'
