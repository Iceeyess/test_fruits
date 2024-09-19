from rest_framework import permissions


class IsNotAdmin(permissions.BasePermission):
    def has_permission(self, request, view):
        return not super().has_permission(request, view)

class IsOwnerOrStaff(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.user.is_staff or request.user == view.get_object().owner:
            return True
        return False
