from rest_framework import serializers
from .models import Note, Comment
from django.contrib.auth import get_user_model


class CommentSerializer(serializers.ModelSerializer):
    author = serializers.ReadOnlyField(source="author.username")

    class Meta:
        fields = (
            "id",
            "author",
            "note",
            "content",
            "created_at",
        )
        model = Comment


# doesn't include comments
class NoteListSerializer(serializers.ModelSerializer):
    author = serializers.ReadOnlyField(source="author.username")

    class Meta:
        fields = (
            "id",
            "author",
            "title",
            "description",
            "created_at",
        )
        model = Note


# for a detailed view, includes comments
class NoteDetailSerializer(serializers.ModelSerializer):
    author = serializers.ReadOnlyField(source="author.username")
    comments = CommentSerializer(many=True, read_only=True)

    class Meta:
        fields = (
            "id",
            "author",
            "title",
            "description",
            "created_at",
            "comments",
        )
        model = Note


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        fields = (
            "id",
            "username",
        )
        model = get_user_model()
