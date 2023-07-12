from django.shortcuts import render
from rest_framework import generics, permissions
from .models import Note
from .serializers import NoteSerializer
from .permissions import IsAutorOrReadOnly


# Create your views here.
class NoteList(generics.ListCreateAPIView):
    queryset = Note.objects.all()
    serializer_class = NoteSerializer
    permission_classes = (IsAutorOrReadOnly,)


class NoteDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Note.objects.all()
    serializer_class = NoteSerializer
    permission_classes = (IsAutorOrReadOnly,)
