from django.shortcuts import render
from rest_framework import generics, permissions, viewsets
from .models import Note, Comment
from .serializers import (
    NoteListSerializer,
    NoteDetailSerializer,
    UserSerializer,
    CommentSerializer,
)
from .permissions import IsAutorOrReadOnly
from django.contrib.auth import get_user_model


# Create your views here.


class UserViewset(viewsets.ModelViewSet):
    queryset = get_user_model().objects.all()
    serializer_class = UserSerializer
    permission_classes = (permissions.IsAdminUser,)


class CommentViewset(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = (IsAutorOrReadOnly,)

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class NoteListView(generics.ListCreateAPIView):
    queryset = Note.objects.all()
    serializer_class = NoteListSerializer
    permission_classes = (IsAutorOrReadOnly,)

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class NoteDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Note.objects.all()
    serializer_class = NoteDetailSerializer
    permission_classes = (IsAutorOrReadOnly,)


# class UserList(generics.ListCreateAPIView):
#     queryset = get_user_model().objects.all()
#     serializer_class = UserSerializer


# class UserDetail(generics.RetrieveUpdateDestroyAPIView):
#     queryset = get_user_model().objects.all()
#     serializer_class = UserSerializer
