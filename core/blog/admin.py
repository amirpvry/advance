from django.contrib import admin
from .models import Categories, Post


class PostAdmin(admin.ModelAdmin):

    list_display = (
        "title",
        "author",
        "create_date",
        "status",
        "categories",
        "publish_date",
    )
    list_filter = ("status", "create_date", "categories")
    search_fields = ("title", "content")
    date_hierarchy = "publish_date"
    ordering = ("-publish_date",)
    filter_horizontal = ("tags",)  # نمایش تگ‌ها در پنل ادمین


# Register your models here.

admin.site.register(Post, PostAdmin)
admin.site.register(Categories)
