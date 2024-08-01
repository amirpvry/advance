from django.urls import path, include
from .views import home_view,about_view,trademark,online_service,copyright_view,design_view,ipserver_view,translation_view


app_name = "main"

urlpatterns = [
    path('', home_view, name='home'),
    path('about', about_view, name='home'),
    path('trade', trademark, name='trade'),
    path('online-service', online_service, name='online-service'),
    path('translation', translation_view, name='translation'),
    path('ip-server', ipserver_view, name='ip-server'),
    path('design', design_view, name='design'),
    path('copyright', copyright_view, name='copyright'),
    
]
