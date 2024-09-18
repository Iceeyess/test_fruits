from rest_framework.permissions import IsAdminUser


class IsNotAdmin(IsAdminUser):
    def has_permission(self, request, view):
        return not super().has_permission(request, view)