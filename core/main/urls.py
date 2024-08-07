from django.urls import path, include
from .views import (
    home_view,
    about_view,
    trademark,
    online_service,
    copyright_view,
    design_view,
    ipserver_view,
    translation_view,
    fa_copyright_view,
    homepage_view,
    services_view,
    about_us_view,
    contact_us_view,
)

app_name = "main"

urlpatterns = [
    path("en/patent", home_view, name="patent"),
    path("en/about", about_view, name="homes"),
    path("en/trade", trademark, name="trade"),
    path("en/online-service", online_service, name="online-service"),
    path("en/translation", translation_view, name="translation"),
    path("en/ip-server", ipserver_view, name="ip-server"),
    path("en/design", design_view, name="design"),
    path("en/copyright", copyright_view, name="copyright"),
    path("fa/copyright", fa_copyright_view, name="fa_copyright"),
    path("", homepage_view, name="homepage"),
    path("en/services", services_view, name="services"),
    path("en/about_us", about_us_view, name="about_us"),
    path("en/contact_us", contact_us_view, name="contact_us"),
]
