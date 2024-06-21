from rest_framework.permissions import BasePermission


class IsSeller(BasePermission):
    """Проверяет, имеет ли пользователь статус продавца."""

    def has_permission(self, request, view):
        user = request.user
        if user.is_seller is True:
            return True
        return False


class IsSellerObject(BasePermission):
    """Проверяет, является ли продавец, владельцем продукта."""

    def has_object_permission(self, request, view, obj):
        if obj.seller == request.user:
            return True
        return False
