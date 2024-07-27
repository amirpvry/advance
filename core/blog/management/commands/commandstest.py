from django.core.management.base import BaseCommand
from faker import Faker
from accounts.models import User, Profile
from blog.models import Categories, Post

from datetime import datetime


Category_items = [
    "Python",
    "Django",
    "JavaScript",
    "React",
    "Vue",
    "Docker",
]


class Command(BaseCommand):
    help = "Closes the specified poll for voting"

    def __init__(self, *args, **kwargs):
        super(Command, self).__init__(*args, **kwargs)
        self.fake = Faker()

    def handle(self, *args, **options):
        user = User.objects.create_user(
            email=self.fake.email(), password="Test@1234567"
        )
        profile = Profile.objects.get(user=user)
        profile.first_name = self.fake.first_name()
        profile.last_name = self.fake.last_name()
        profile.description = self.fake.text(max_nb_chars=200)
        profile.save()

        for name in Category_items:
            Categories.objects.get_or_create(name=name)

        for i in range(10):
            Post.objects.create(
                author=profile,
                title=self.fake.sentence(nb_words=5),
                content=self.fake.text(max_nb_chars=500),
                categories=Categories.objects.all().order_by("?").first(),
                status=True,
                image=self.fake.image_url(width=640, height=480),
                publish_date=datetime.now(),
            )
