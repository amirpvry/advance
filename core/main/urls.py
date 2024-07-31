from django.urls import path, include
from . import views


app_name = "main"

urlpatterns = [
    path("api/v1/", include("main.api.v1.urls")),
]
