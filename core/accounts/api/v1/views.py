from rest_framework import viewsets, generics
from rest_framework.response import Response
from .serialaizers import (
    RecursionSerializer,
    CustomAuthTokenSerializer,
    ChangePasswordSerializer,
    ProfileSerializer,
    ResentEmailSerializer,
)
from rest_framework import status
from rest_framework.authtoken.views import ObtainAuthToken, APIView
from rest_framework.authtoken.models import Token
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth.models import User
from accounts.models import Profile
from django.shortcuts import get_object_or_404
from django.contrib.auth import logout
from django.core.mail import send_mail
from mail_templated import send_mail
from mail_templated import EmailMessage
from ..utils import Thread
from rest_framework_simplejwt.tokens import RefreshToken
from django.core.mail import send_mail
from django.conf import settings
from rest_framework import generics, status
from django.template.loader import render_to_string
import jwt
from django.conf import settings
from django.contrib.auth import get_user_model


User = get_user_model()


class RegesterationApiView(generics.GenericAPIView):
    serializer_class = RecursionSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()

            # توکن‌ها را برای کاربر جدید دریافت کنید
            tokens = self.get_tokens_for_user(user)

            # محتوای ایمیل را ایجاد کنید
            email_content = render_to_string(
                "email/activation_email.tpl", {"tokens": tokens["access"]}
            )

            # ارسال ایمیل
            send_mail(
                "Your Tokens",
                email_content,
                settings.DEFAULT_FROM_EMAIL,
                [user.email],
                fail_silently=False,
            )

            data = {"email": serializer.validated_data["email"]}
            return Response(data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @staticmethod
    def get_tokens_for_user(user):
        refresh = RefreshToken.for_user(user)
        return {
            # 'refresh': str(refresh),
            "access": str(refresh.access_token),
        }


class CustomAuthToken(ObtainAuthToken):
    serializer_class = CustomAuthTokenSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(
            data=request.data, context={"request": request}
        )
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data["user"]
        token, created = Token.objects.get_or_create(user=user)
        return Response({"token": token.key, "user_id": user.pk, "email": user.email})


class CustomDiscardToken(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, *args, **kwargs):
        try:
            request.user.auth_token.delete()
            return Response(status=status.HTTP_200_OK)
        except Exception as e:
            return Response(str(e), status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class ChangePasswordApiView(generics.GenericAPIView):
    """
    An endpoint for changing password.
    """

    serializer_class = ChangePasswordSerializer
    model = User
    permission_classes = (IsAuthenticated,)

    def get_object(self, queryset=None):
        obj = self.request.user
        return obj

    def put(self, request, *args, **kwargs):
        self.object = self.get_object()
        serializer = self.get_serializer(data=request.data)

        if serializer.is_valid():
            # Check old password
            if not self.object.check_password(serializer.data.get("old_password")):
                return Response(
                    {"old_password": ["Wrong password."]},
                    status=status.HTTP_400_BAD_REQUEST,
                )
            # set_password also hashes the password that the user will get
            self.object.set_password(serializer.data.get("new_password"))
            self.object.save()
            response = {
                "status": "success",
                "code": status.HTTP_200_OK,
                "message": "Password updated successfully",
                "data": [],
            }

            return Response(response)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ProfileApiView(generics.RetrieveUpdateAPIView):
    permission_classes = [IsAuthenticated]

    serializer_class = ProfileSerializer
    queryset = Profile.objects.all()

    def get_object(self):
        queryset = self.get_queryset()
        obj = get_object_or_404(queryset, user=self.request.user)
        return obj


class SendEmailApiView(generics.GenericAPIView):

    def get(self, request, *args, **kwargs):
        user = request.user  # فرض بر اینکه کاربر از طریق احراز هویت درخواست می‌دهد

        if not user.email:
            return Response(
                "User does not have an email",
                status=status.HTTP_400_BAD_REQUEST,
            )

        tokens = self.get_tokens_for_user(user)
        email_content = f"Hello {user.email},\n\nYour access token is: {tokens['access']}\nYour refresh token is: {tokens['refresh']}"

        send_mail(
            "Your Tokens",
            email_content,
            settings.DEFAULT_FROM_EMAIL,
            [user.email],
            fail_silently=False,
        )

        return Response("Email sent", status=status.HTTP_200_OK)

    @staticmethod
    def get_tokens_for_user(user):
        refresh = RefreshToken.for_user(user)
        return {
            "refresh": str(refresh),
            "access": str(refresh.access_token),
        }


# class ActivateApiView(APIView):
#     def get(self, request, token, *args, **kwargs):
#        try:
#             # Decode the token using the secret key
#             decoded_payload = jwt.decode(token, settings.SECRET_KEY, algorithms=['HS256'])

#             # Extract user information from the decoded payload
#             user_id = decoded_payload.get('user_id')
#        except jwt.ExpiredSignatureError:
#         return Response({"error": "Activation link has expired"}, status=status.HTTP_400_BAD_REQUEST)
#        except jwt.InvalidSignatureError:
#         return Response({"error": "Invalid token"}, status=status.HTTP_400_BAD_REQUEST)
#        except Exception as e:
#         return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

#        user_obj = User.objects.get(pk=user_id)
#        user_obj = user_obj.is_verified = True
#        user_obj.save()
#        return Response({"message": "Account successfully activated"}, status=status.HTTP_200_OK)


# if not user_id:
#     return Response({"error": "Invalid token payload"}, status=status.HTTP_400_BAD_REQUEST)

# # Find the user by the extracted user_id
# try:
#     user = User.objects.get(id=user_id)
# except User.DoesNotExist:
#     return Response({"error": "User not found"}, status=status.HTTP_404_NOT_FOUND)

# # Check if the user's account is already active
# if user.is_active:
#     return Response({"message": "Account already activated"}, status=status.HTTP_200_OK)

# # Activate the user's account
# user.is_active = True
# user.save()

# return Response({"message": "Account successfully activated"}, status=status.HTTP_200_OK)


class ActivateApiView(APIView):
    def get(self, request, tokens, *args, **kwargs):
        try:
            # Decode the token using the secret key
            decoded_payload = jwt.decode(
                tokens, settings.SECRET_KEY, algorithms=["HS256"]
            )

            # Extract user information from the decoded payload
            user_id = decoded_payload.get("user_id")

            if not user_id:
                return Response(
                    {"error": "Invalid token payload"},
                    status=status.HTTP_400_BAD_REQUEST,
                )

            # Find the user by the extracted user_id
            try:
                user = User.objects.get(id=user_id)
            except User.DoesNotExist:
                return Response(
                    {"error": "User not found"},
                    status=status.HTTP_404_NOT_FOUND,
                )

            # Check if the user's account is already active
            if user.is_active:
                return Response(
                    {"message": "Account already activated"},
                    status=status.HTTP_200_OK,
                )

            # Activate the user's account
            user.is_active = True
            user.is_verified = True
            #        user_obj.save()
            user.save()

            return Response(
                {"message": "Account successfully activated"},
                status=status.HTTP_200_OK,
            )

        except jwt.ExpiredSignatureError:
            return Response(
                {"error": "Activation link has expired"},
                status=status.HTTP_400_BAD_REQUEST,
            )
        except jwt.DecodeError:
            return Response(
                {"error": "Invalid token"}, status=status.HTTP_400_BAD_REQUEST
            )
        except Exception as e:
            return Response(
                {"error": str(e)},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR,
            )


class ResentEmailApiView(generics.GenericAPIView):
    serializer_class = ResentEmailSerializer

    def get(self, request, *args, **kwargs):
        # گرفتن داده‌های query parameters و اعتبارسنجی آنها
        serializer = self.get_serializer(data=request.query_params)
        serializer.is_valid(raise_exception=True)
        email = serializer.validated_data["email"]  # استخراج ایمیل پس از اعتبارسنجی

        try:
            # جستجو برای کاربر با ایمیل مشخص شده
            user = User.objects.get(email=email)
        except User.DoesNotExist:
            # اگر کاربری با این ایمیل پیدا نشد، برگرداندن پیغام خطا
            return Response(
                {"error": "User with this email does not exist."},
                status=status.HTTP_404_NOT_FOUND,
            )

        # تولید توکن‌های جدید برای کاربر
        tokens = self.get_tokens_for_user(user)

        # ایجاد محتوای ایمیل با استفاده از قالب و توکن‌های جدید
        email_content = render_to_string(
            "email/activation_email.tpl",
            {"tokens": tokens["access"], "user": user},
        )

        # ارسال ایمیل
        send_mail(
            "Your Tokens",
            email_content,
            settings.DEFAULT_FROM_EMAIL,
            [user.email],
            fail_silently=False,
        )

        # برگرداندن پیغام موفقیت
        return Response(
            {"message": "Activation email has been resent."},
            status=status.HTTP_200_OK,
        )

    @staticmethod
    def get_tokens_for_user(user):
        # تولید و برگرداندن توکن‌های جدید برای کاربر
        refresh = RefreshToken.for_user(user)
        return {
            "access": str(refresh.access_token),
        }
