from .views import UserViewset, NoteViewset
from rest_framework.routers import SimpleRouter, DefaultRouter

router = SimpleRouter()
router.register("users", UserViewset, basename="users")
router.register("", NoteViewset, basename="notes")

urlpatterns = router.urls

# from django.urls import path
# from .views import NoteList, NoteDetail, UserList, UserDetail

# urlpatterns = [
#     path("<int:pk>/", NoteDetail.as_view(), name="note_detail"),
#     path("", NoteList.as_view(), name="note_list"),
#     path("users/<int:pk>/", UserDetail.as_view(), name="user_detail"),
#     path("users/", UserList.as_view(), name="user_list"),
# ]
