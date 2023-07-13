from django.contrib import admin
from .models import Note, Comment


class NoteAdmin(admin.ModelAdmin):
    model = Note
    list_display = ["title", "id", "author"]


class CommentAdmin(admin.ModelAdmin):
    model = Comment
    list_display = ["id", "note", "author"]


admin.site.register(Note, NoteAdmin)
admin.site.register(Comment, CommentAdmin)
