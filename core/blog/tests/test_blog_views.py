from django.test import TestCase, Client
from django.urls import reverse
from ..models import Post, Categories
from accounts.models import Profile, User

class TestView(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(email="test@example.com", password="a/@1234567")
        self.profile = Profile.objects.create(
            user=self.user,
            first_name="asdadasd",
            last_name="asdasdasdadasd",
            description="description"
        )
        self.post = Post.objects.create(
            author=self.profile,
            title="Test Post",
            content="This is a test post."
        )
    def test_home_status_view(self):
        url = reverse('blog:post-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)


    # def test_post_anonymous_status_view(self):
    #     url = reverse('blog:post-detail', kwargs={'pk': self.post.id})
    #     print(f"URL: {url}")  # چاپ URL برای اطمینان
    #     response = self.client.get(url)
    #     self.assertEqual(response.status_code, 200)