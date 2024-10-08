from django.test import TestCase


from ..models import Categories
from ..forms import PostForm


# Create your tests here.
class PostFormTest(TestCase):
    def test_form_post_with_valid_data(self):
        categories = Categories.objects.create(name="test ")
        form = PostForm(
            data={
                "title": "Test Post",
                "content": "This is a test post.",
                "categories": categories,
            }
        )
        self.assertFalse(form.is_valid())
