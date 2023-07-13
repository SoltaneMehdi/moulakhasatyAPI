from django.shortcuts import render
from rest_framework import generics, permissions, viewsets
from .models import Note
from .serializers import NoteSerializer, UserSerializer
from .permissions import IsAutorOrReadOnly
from django.contrib.auth import get_user_model


# Create your views here.
class NoteViewset(viewsets.ModelViewSet):
    queryset = Note.objects.all()
    serializer_class = NoteSerializer
    permission_classes = (IsAutorOrReadOnly,)


class UserViewset(viewsets.ModelViewSet):
    queryset = get_user_model().objects.all()
    serializer_class = UserSerializer
    permission_classes = (permissions.IsAdminUser,)


# class NoteList(generics.ListCreateAPIView):
#     queryset = Note.objects.all()
#     serializer_class = NoteSerializer
#     permission_classes = (IsAutorOrReadOnly,)


# class NoteDetail(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Note.objects.all()
#     serializer_class = NoteSerializer
#     permission_classes = (IsAutorOrReadOnly,)


# class UserList(generics.ListCreateAPIView):
#     queryset = get_user_model().objects.all()
#     serializer_class = UserSerializer


# class UserDetail(generics.RetrieveUpdateDestroyAPIView):
#     queryset = get_user_model().objects.all()
#     serializer_class = UserSerializer
