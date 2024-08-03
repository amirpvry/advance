from django.db import models


from django.urls import reverse
# from taggit.managers import TaggableManager

# Create your models here.

# User = get_user_model()


class Post(models.Model):

    author = models.ForeignKey("accounts.Profile", on_delete=models.CASCADE)

    title = models.CharField(max_length=256)

    content = models.TextField()
    categories = models.ForeignKey("Categories", on_delete=models.SET_NULL, null=True)
    # tags = TaggableManager()


    status = models.BooleanField(default=False)
    image = models.ImageField(null=True, blank=True)
    publish_date = models.DateTimeField(null=True)
    create_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return self.title

    # def get_absolute_api_url(self):
    #     return reverse('blog:api-v1:post-detail', kwargs={'pk': self.pk})
    def get_absolute_api_url(self):
        return reverse("blog:api-v1:post-detail", kwargs={"pk": self})
    def get_absolute_url(self):
        return reverse("blog:post-detail", kwargs={"pk": self.pk})


class Categories(models.Model):
    name = models.CharField(max_length=256)

    def __str__(self):
        return self.name
