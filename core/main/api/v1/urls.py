# urls.py
from django.urls import path
from .views import MainModelViewSet

main_list = MainModelViewSet.as_view({
    'get': 'list',
    'post': 'create'
})

main_detail = MainModelViewSet.as_view({
    'get': 'retrieve',
    'put': 'update',
    'patch': 'partial_update',
    'delete': 'destroy'
})

app_name = "api-v1"


urlpatterns = [
    path('/mainpost/', main_list, name='mainpost-list'),
    path('/mainpost/<int:pk>/', main_detail, name='mainpost-detail'),
]
