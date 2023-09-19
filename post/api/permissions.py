from rest_framework.permissions import BasePermission

class IsOwner(BasePermission):
    message = "Bu işlemi yapmaya yetkiniz yok!"
    def has_object_permission(self, request, view, obj):
        if request.user == obj.user:
            return True
        return False