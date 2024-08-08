from django.urls import path, include
from .views import *

app_name = "main"

urlpatterns = [
    path("en/patent", home_view, name="patent"),
    path("fa/patent", fa_home_view, name="patent_fa"),
    # path("en/about", about_view, name="homes"),
    path("en/trade", trademark, name="trade"),
    path("fa/trade", fa_trademark, name="trade_fa"),

    path("en/online-service", online_service, name="online-service"),
    path("fa/online-service", fa_online_service, name="online-service_fa"),

    path("en/translation", translation_view, name="translation"),
    path("fa/translation", fa_translation_view, name="translation_fa"),

    path("en/ip-server", ipserver_view, name="ip-server"),
    path("fa/ip-server", fa_ipserver_view, name="ip-server_fa"),

    path("en/design", design_view, name="design"),
    path("fa/design", fa_design_view, name="design_fa"),

    path("en/copyright", copyright_view, name="copyright"),
    path("fa/copyright", fa_copyright_view, name="copyright_fa"),

    path("en/", homepage_view, name="homepage"),
    path("fa/", fa_homepage_view, name="homepage_fa"),

    path("en/services", services_view, name="services"),
    path("fa/services", fa_services_view, name="services_fa"),

    path("en/about_us", about_us_view, name="about_us"),
    path("fa/about_us", fa_about_us_view, name="about_us_fa"),
    
    path("en/contact_us", contact_us_view, name="contact_us"),
    path("fa/contact_us", fa_contact_us_view, name="contact_us_fa"),
]
