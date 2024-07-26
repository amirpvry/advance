import pytest
from rest_framework.test import APIClient
from django.urls import reverse
from accounts.models import User

import datetime

@pytest.fixture

def common_user():
    user = User.objects.create_user(
        email='testuser@example.com',
        password='test123', is_verified=True
    )
    return user
    



@pytest.mark.django_db
class TestPostApi:
    def test_post_api_create(self):
        client = APIClient()
        url = reverse('blog:api-v1:post-list')
        response = client.get(url)
        assert response.status_code == 200

    def test_post_create_status_code_201(self, common_user):
        client = APIClient()
        url = reverse('blog:api-v1:post-list')
        data = {
            'title': 'Test Post',
            'content': 'This is a test post.',
            'status': True ,
            "create_date" : datetime.datetime
            
        }
        client.force_authenticate(user= common_user)
        response = client.post(url, data)
        assert response.status_code == 201


