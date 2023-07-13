from rest_framework import serializers
from .models import Note
from django.contrib.auth import get_user_model


class NoteSerializer(serializers.ModelSerializer):
    class Meta:
        fields = (
            "id",
            "author",
            "title",
            "description",
            "created_at",
        )
        model = Note


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        fields = (
            "id",
            "username",
        )
        model = get_user_model()
