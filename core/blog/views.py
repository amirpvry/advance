from django.shortcuts import render
from django.views.generic import (
    TemplateView,
    RedirectView,
    DetailView,
    CreateView,
    UpdateView,
)
from blog.models import Post
from django.shortcuts import get_object_or_404
from django.views.generic.list import ListView
from .forms import PostForm
from django.views.generic.edit import DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import ValidationError
from accounts.models import Profile
from blog.models import Post


# Create your views here.
def indexview(request):
    return render(request, "index.html")


class IndexView(TemplateView):
    template_name = "index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["name"] = "index"
        context["post"] = Post.objects.all()
        return context


class Redirecttodjango(RedirectView):

    url = "http://django.org/redirect"

    def get_redirect_url(self, *args, **kwargs):
        post = get_object_or_404(Post, pk=kwargs["pk"])

        return super().get_redirect_url(*args, **kwargs)


class PostList(ListView):
    # model = Post
    context_object_name = "posts"
    paginate_by = 1
    # ordering = '-id'

    def get_queryset(self):
        return Post.objects.filter(status=True)


class PostDetailView(DetailView):
    model = Post


class PostCreateView(CreateView):
    model = Post
    fields = ["title", "content", "status", "categories"]
    success_url = "/blog/post/"

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class PostUpdateView(UpdateView):
    model = Post
    form_class = PostForm
    success_url = "/blog/post/"


class PostDeleteView(LoginRequiredMixin, DeleteView):
    model = Post
    success_url = "/blog/post/"
