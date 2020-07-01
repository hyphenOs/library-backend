# Copyright (c) 2020 hyphenOs Software Labs Private Limited

from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from library import views

urlpatterns = [
    path('books/', views.BookList.as_view()),
    path('books/<int:pk>/', views.BookDetail.as_view()),
    path('members/', views.MemberList.as_view()),
    path('members/<int:pk>/', views.MemberDetail.as_view())
]

urlpatterns = format_suffix_patterns(urlpatterns)
