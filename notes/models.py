from django.db import models
from django.conf import settings
from django.core.files.storage import default_storage


def upload_to(instance, filename):
    return "note_files/{filename}".format(filename=filename)


# Create your models here.
class Note(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField(max_length=200)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    likes = models.ManyToManyField(
        settings.AUTH_USER_MODEL, related_name="liked_posts", blank=True
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    note_files = models.FileField(upload_to=upload_to, blank=True, null=True)

    def __str__(self):
        return self.title

    def total_likes(self):
        return self.likes.count()

    def delete_note_files(sender, instance, **kwargs):
        default_storage.delete(instance.file.path)


class Comment(models.Model):
    note = models.ForeignKey(Note, on_delete=models.CASCADE, related_name="comments")
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    content = models.TextField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.id
