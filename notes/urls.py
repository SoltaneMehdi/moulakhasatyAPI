from .views import UserViewset, NoteListView, NoteDetailView, CommentViewset
from rest_framework.routers import SimpleRouter, DefaultRouter
from django.urls import path, include


router = SimpleRouter()
router.register("users", UserViewset, basename="users")
router.register("comments", CommentViewset, basename="comments")

urlpatterns = [
    path("<int:pk>/", NoteDetailView.as_view(), name="note_detail"),
    path("", NoteListView.as_view(), name="note_list"),
    path("", include(router.urls)),
]
