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


# for a detailed view, includes comments
class NoteSerializer(serializers.ModelSerializer):
    author = serializers.ReadOnlyField(source="author.username")
    comments = CommentSerializer(many=True, read_only=True)
    likes = serializers.SerializerMethodField()
    liked = serializers.SerializerMethodField()
    note_files = serializers.FileField(required=False)

    class Meta:
        fields = (
            "id",
            "author",
            "title",
            "description",
            "created_at",
            "comments",
            "likes",
            "liked",
            "note_files",
        )
        model = Note

    def get_likes(self, obj):
        return obj.total_likes()

    def get_liked(self, obj):
        request = self.context.get("request", None)
        if request and request.user.is_authenticated:
            return obj.likes.filter(id=request.user.id).exists()
        return False


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        fields = (
            "id",
            "username",
        )
        model = get_user_model()
