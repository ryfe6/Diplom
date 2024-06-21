from rest_framework.serializers import ModelSerializer

from users.models import User


class UserSerializer(ModelSerializer):
    """Сериалайзер для работы с пользователями."""

    class Meta:
        model = User
        fields = "__all__"
