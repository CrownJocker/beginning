from rest_framework.permissions import BasePermission, SAFE_METHODS, IsAuthenticated


class ReadPerm(BasePermission):
    message = "Hello there"

    def has_permission(self, request, view):
        if request.method in SAFE_METHODS:
            return bool(request.user and request.user.is_authenticated)

