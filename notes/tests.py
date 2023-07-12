from django.test import TestCase
from .models import Note
from django.contrib.auth import get_user_model


# Create your tests here.
class NoteTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.user = get_user_model().objects.create_user(
            username="testUser", email="test@email.com", password="secret"
        )
        cls.note = Note.objects.create(
            author=cls.user, title="a good title", description="explaining the note"
        )

    def test_note_model(self):
        self.assertEqual(self.note.author.username, "testUser")
        self.assertEqual(self.note.title, "a good title")
        self.assertEqual(self.note.description, "explaining the note")
        self.assertEqual(str(self.note), "a good title")
