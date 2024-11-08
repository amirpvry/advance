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
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from taggit.models import Tag


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
    

from django.core.paginator import Paginator

class PostList(ListView):
    context_object_name = "posts"
    paginate_by = 3

    def get_queryset(self):
        queryset = Post.objects.filter(status=True)
        tag_name = self.request.GET.get('tag')
        if tag_name:
            tag = get_object_or_404(Tag, name=tag_name)
            queryset = queryset.filter(tags=tag)
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        tags = Tag.objects.all()
        paginator = Paginator(tags, 10)  # برای صفحه‌بندی تگ‌ها
        page = self.request.GET.get('page')
        try:
            tags = paginator.page(page)
        except PageNotAnInteger:
            tags = paginator.page(1)
        except EmptyPage:
            tags = paginator.page(paginator.num_pages)
        context['tags'] = tags  # صفحه‌بندی تگ‌ها
        return context


class Redirecttodjango(RedirectView):

    url = "http://django.org/redirect"

    def get_redirect_url(self, *args, **kwargs):
        post = get_object_or_404(Post, pk=kwargs["pk"])

        return super().get_redirect_url(*args, **kwargs)




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


def blog_posting(request):
    posts = Post.objects.filter(
        status=True
    )  # فرض می‌کنیم که فقط پست‌های منتشر شده را نمایش می‌دهیم
    return render(request, "blog/blog-posting.html", {"posts": posts})


def fa_blog_posting(request):
    posts = Post.objects.filter(
        status=True
    )  # فرض می‌کنیم که فقط پست‌های منتشر شده را نمایش می‌دهیم
    return render(request, "blog/fa_blog_posting.html", {"posts": posts})

def blog_soon(request):
    return render(request, "blog/blog-soon.html")


def fa_blog_soon(request):
    return render(request, "blog/fa_blog-soon.html")


from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

def tagged_posts(request, name):
    tag = get_object_or_404(Tag, name=name)
    posts_list = Post.objects.filter(tags=tag)
    paginator = Paginator(posts_list, 3)
    page = request.GET.get('page')

    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)

    return render(request, "blog/blog-posting.html", {"posts": posts, "tag": tag})

