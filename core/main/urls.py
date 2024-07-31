from django.urls import path, include
from .views import home_view,about_view


app_name = "main"

urlpatterns = [
    path('', home_view, name='home'),
    path('about', about_view, name='home'),
    
]
