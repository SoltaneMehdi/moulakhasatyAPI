from django.shortcuts import render
from rest_framework import generics, permissions, viewsets, status, views
from rest_framework.response import Response
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.exceptions import ValidationError
from .models import Note, Comment
from .serializers import UserSerializer, NoteSerializer, CommentSerializer
from .permissions import IsAutorOrReadOnly
from django.contrib.auth import get_user_model
import zipfile


# Create your views here.


class UserViewset(viewsets.ModelViewSet):
    queryset = get_user_model().objects.all()
    serializer_class = UserSerializer
    permission_classes = (permissions.IsAdminUser,)


class NoteViewset(viewsets.ModelViewSet):
    queryset = Note.objects.all()
    serializer_class = NoteSerializer
    permission_classes = (IsAutorOrReadOnly,)
    parser_classes = [MultiPartParser, FormParser]

    def perform_create(self, serializer):
        file = self.request.FILES.get("note_files")
        if file:
            print("file sent")
            if zipfile.is_zipfile(file):
                print("is a zip file")
            else:
                print("not a zip file")
                raise ValidationError("not a zip file")
        serializer.save(author=self.request.user)

    def perform_update(self, serializer):
        file = self.request.FILES.get("note_files")
        if file:
            print("file sent")
            if zipfile.is_zipfile(file):
                print("is a zip file")
            else:
                print("not a zip file")
                raise ValidationError("not a zip file")
        serializer.save(author=self.request.user)

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response(status=status.HTTP_204_NO_CONTENT)

    def perform_destroy(self, instance):
        # Delete associated file(s) here
        instance.note_files.delete()
        instance.delete()


class LikeNoteView(views.APIView):
    def post(self, request, pk):
        note = Note.objects.get(pk=pk)
        note.likes.add(request.user)
        note.save()
        return Response({"detail": "post liked."}, status=status.HTTP_200_OK)


class UnlikeNoteView(views.APIView):
    def post(self, request, pk):
        note = Note.objects.get(pk=pk)
        note.likes.remove(request.user)
        note.save()
        return Response({"detail": "post unliked."}, status=status.HTTP_200_OK)


class CommentViewset(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = (IsAutorOrReadOnly,)

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


# class UserList(generics.ListCreateAPIView):
#     queryset = get_user_model().objects.all()
#     serializer_class = UserSerializer


# class UserDetail(generics.RetrieveUpdateDestroyAPIView):
#     queryset = get_user_model().objects.all()
#     serializer_class = UserSerializer
