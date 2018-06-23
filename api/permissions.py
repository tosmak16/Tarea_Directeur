from rest_framework.permissions import BasePermission
from .models import Tarea


class IsOwner(BasePermission):
    """Custom permission class to allow only a tarea owners to edit them."""

    def has_object_permission(self, request, view, obj):
        """Return True if permission is granted to the tarea owner."""
        if isinstance(obj, Tarea):
            return obj.owner == request.user
        return obj.owner == request.user