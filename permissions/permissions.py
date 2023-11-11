from rest_framework.permissions import SAFE_METHODS, IsAuthenticated

MEMBERS_METHODS = ('GET', 'OPTIONS')


class IsHeadOfDepartment(IsAuthenticated):
    def has_permission(self, request, view):
        if (
            request.user.position == 1
            or request.user.is_superuser
            or request.user.is_admin
        ):
            return True

        if request.user.position and request.user.position.id == 1:
            return True
        return False


class IsMembers(IsAuthenticated):
    def has_permission(self, request, view):
        if (
            request.user.position == 1
            or request.user.is_superuser
            or request.user.is_admin
        ):
            return True

        if request.user.position and request.user.is_staff:
            return True
        return False
