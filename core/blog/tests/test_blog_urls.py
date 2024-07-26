from django.test import TestCase, SimpleTestCase
from django.urls import reverse, resolve
from blog.views import PostDetailView


# Create your tests here.
class TestUrl(SimpleTestCase):

    def test_blog_url(self):
        url = reverse("blog:post-detail", kwargs={"pk": 1})
        self.assertEqual(resolve(url).func.view_class, PostDetailView)
