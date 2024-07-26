from django.contrib import admin
from .models import Categories, Post


class Postadmin(admin.ModelAdmin):
    list_display = ("title", "author", "created_at", "status")


# Register your models here.
admin.site.register(Post)
admin.site.register(Categories)
