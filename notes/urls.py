from .views import (
    UserViewset,
    NoteViewset,
    LikeNoteView,
    UnlikeNoteView,
    CommentViewset,
)
from rest_framework.routers import SimpleRouter, DefaultRouter
from django.urls import path, include


router = SimpleRouter()
router.register("users", UserViewset, basename="users")
router.register("notes", NoteViewset, basename="notes")
router.register("comments", CommentViewset, basename="comments")

urlpatterns = [
    path("<int:pk>/like", LikeNoteView.as_view(), name="like_note"),
    path("<int:pk>/unlike", UnlikeNoteView.as_view(), name="unlike_note"),
    path("", include(router.urls)),
]
