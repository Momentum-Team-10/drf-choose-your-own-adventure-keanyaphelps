from collections import UserList
from django.shortcuts import render
from rest_framework import generics, serializers
from rest_framework.viewsets import ModelViewSet
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse
from .models import Book, User
from .serializers import BookSerializer, UserSerializer



@api_view(['GET'])
def api_root(request, format=None):
    return Response({
        'users': reverse('user-list', request=request, format=format),
        'books': reverse('book-list', request=request, format=format),
    })

class BookViewSet(ModelViewSet):
    queryset = Book.objects.all()
    serializers_class = BookSerializer

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class BookDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Book.objects.all()
    serializers_class = BookSerializer

class UserList(generics):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserDetail(generics.RetrieveAPIView):
    queryset = User.objects.all
    serializer_class = UserSerializer

