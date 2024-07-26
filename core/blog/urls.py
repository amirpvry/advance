from django.urls import path, include
from . import views
from django.views.generic import TemplateView
from django.views.generic.base import RedirectView

app_name = "blog"

urlpatterns = [
    path("fbv-index", views.indexview, name="fbv-index"),
    # path('cbv-index', TemplateView.as_view(template_name="index.html",extra_context={"name":"index"}))
    path("cbv-index", views.IndexView.as_view(), name="cbv-index"),
    path(
        "go-to-django/<int:pk>/",
        views.Redirecttodjango.as_view(),
        name="go-to-django",
    ),
    path("post/", views.PostList.as_view(), name="post-list"),
    path("post/<int:pk>", views.PostDetailView.as_view(), name="post-detail"),
    path("post/create/", views.PostCreateView.as_view(), name="post-create"),
    path(
        "post/<int:pk>/update/",
        views.PostUpdateView.as_view(),
        name="post-update",
    ),
    path(
        "post/<int:pk>/delete/",
        views.PostDeleteView.as_view(),
        name="post-delete",
    ),
    path("api/v1/", include("blog.api.v1.urls")),
]
