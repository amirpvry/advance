from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User, Profile


# Register your models here.
class CustomUserAdmin(UserAdmin):

    list_display = ("email", "is_staff", "is_active", "is_verified")
    list_filter = (
        "email",
        "is_staff",
        "is_active",
    )
    fieldsets = (
        ("Authentications", {"fields": ("email", "password")}),
        (
            "Permissions",
            {
                "fields": (
                    "is_staff",
                    "is_active",
                    "is_superuser",
                    "is_verified",
                )
            },
        ),
        ("GroupPermissions", {"fields": ("groups", "user_permissions")}),
        ("importan dates", {"fields": ("last_login",)}),
    )

    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": (
                    "email",
                    "password1",
                    "password2",
                    "is_staff",
                    "is_active",
                    "is_superuser",
                    "is_verified",
                ),
            },
        ),
    )
    search_fields = ("email",)
    ordering = ("email",)


admin.site.register(Profile)
admin.site.register(User, CustomUserAdmin)
