from django.urls import path, include
from . import views
from django.views.generic import TemplateView
from django.views.generic.base import RedirectView
from rest_framework.routers import DefaultRouter
from .views import PostViewSetModel, CategorySetModel

app_name = "api-v1"


router = DefaultRouter()
router.register("post", PostViewSetModel, basename="post")
router.register("category", CategorySetModel, basename="category")

urlpatterns = router.urls
