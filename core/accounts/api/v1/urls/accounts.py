from django.urls import path, include
from .. import views
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView,
)


urlpatterns = [
    path(
        "registration",
        views.RegesterationApiView.as_view(),
        name="registration",
    ),
    path("token/login", views.CustomAuthToken.as_view(), name="token-login"),
    path(
        "token/logout",
        views.CustomDiscardToken.as_view(),
        name="token-logout",
    ),
    path("jwt/create", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("jwt/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
    path("jwt/verify/", TokenVerifyView.as_view(), name="token_verify"),
    path(
        "Change-Password",
        views.ChangePasswordApiView.as_view(),
        name="change_password",
    ),
    path("send-email", views.SendEmailApiView.as_view(), name="send_email"),
    path(
        "activation/confirm/<str:tokens>",
        views.ActivateApiView.as_view(),
        name="activate",
    ),
    path(
        "resent-email",
        views.ResentEmailApiView.as_view(),
        name="resent_email",
    ),
]
