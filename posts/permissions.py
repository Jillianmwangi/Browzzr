from rest_framework import permissions
from rest_framework.permissions import BasePermission



class IsAuthorOrReadOnly(permissions.BasePermission):
    """
    Custom permission to only allow authors of an object to edit or delete it.
    """
    
    def has_object_permission(self, request, view, obj):
        # SAFE_METHODS include GET, HEAD, OPTIONS (read-only methods)
        if request.method in permissions.SAFE_METHODS:
            return True

        # Write permissions are only allowed to the author of the post/comment.
        return obj.author == request.user
