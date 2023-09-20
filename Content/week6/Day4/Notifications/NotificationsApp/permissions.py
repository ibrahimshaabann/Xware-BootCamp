from rest_framework.permissions import BasePermission
from .models import User  # Assuming the User model is in the authentication app

class RolePermissions(BasePermission):
    """
    Custom permission class to check user role and object ownership.

    This permission class is used to control access to specific views or objects based on
    the user's role and ownership of the object.

    Attributes:
        None

    Methods:
        has_permission(request, view): Check if the user has a specific role.
        has_object_permission(request, view, obj): Check if the user owns the object.
    """
    def has_permission(self, request, view):
        """
        Check if the user has a specific role.

        Args:
            request (HttpRequest): The incoming HTTP request.
            view (View): The view being accessed.

        Returns:
            bool: True if the user has the required role, False otherwise.
        """
        print("test")
        print(request.user)
        return request.user.role == User.Roles.SUPERUSER

    def has_object_permission(self, request, view, obj):
        """
        Check if the user owns the object.

        Args:
            request (HttpRequest): The incoming HTTP request.
            view (View): The view being accessed.
            obj: The object being accessed.

        Returns:
            bool: True if the user owns the object, False otherwise.
        """
        return obj.user == request.user
