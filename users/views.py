from rest_framework.generics import CreateAPIView, ListAPIView, UpdateAPIView
from rest_framework.permissions import IsAdminUser, IsAuthenticated

from users.models import User
from users.serializer import UserSerializer


class UserCreateApiView(CreateAPIView):
    """Регистрация пользователя."""

    serializer_class = UserSerializer
    queryset = User.objects.all()

    def perform_create(self, serializer):
        """Переводим пользователя в статус активного пользователя."""
        user = serializer.save(is_active=True)
        user.set_password(user.password)
        user.save()


class UserListApiView(ListAPIView):
    """Просмотреть всех пользователей."""

    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated, IsAdminUser]


class UserUpdateApiView(UpdateAPIView):
    """Изменить информацию о пользователе."""

    queryset = User.objects.all()
    serializer_class = UserSerializer
