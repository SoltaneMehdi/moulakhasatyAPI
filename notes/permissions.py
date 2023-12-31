from rest_framework import permissions


class IsAutorOrReadOnly(permissions.BasePermission):
    def has_permission(self, request, view):
        # unauthenticated users do read only
        if request.method in permissions.SAFE_METHODS:
            return True
        return request.user.is_authenticated

    def has_object_permission(self, request, view, obj):
        # Read permissions are allowed to any request so we'll always
        # allow GET, HEAD, or OPTIONS requests
        if request.method in permissions.SAFE_METHODS:
            return True

        # write permissions are only allowed to the author of a object
        return obj.author == request.user or request.user.is_superuser
