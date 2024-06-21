from django.urls import path
from rest_framework.permissions import AllowAny
from rest_framework_simplejwt.views import (TokenObtainPairView,
                                            TokenRefreshView)

from users.apps import UsersConfig
from users.views import UserCreateApiView, UserListApiView

app_name = UsersConfig.name

urlpatterns = [
    path("", UserListApiView.as_view(), name="user_list"),
    path(
        "register/",
        UserCreateApiView.as_view(permission_classes=(AllowAny,)),
        name="register",
    ),
    path("update/<int:pk>/", UserCreateApiView.as_view(), name="user_update"),
    path("login/", TokenObtainPairView.as_view(), name="login"),
    path("token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
]
