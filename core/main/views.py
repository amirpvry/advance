from django.shortcuts import render


def home_view(request):
    return render(request, "main/patent.html")


def fa_home_view(request):
    return render(request, "main/fa_patent.html")


# def about_view(request):
#     return render(request, "main/about.html")


def trademark(request):
    return render(request, "main/trademark.html")


def fa_trademark(request):
    return render(request, "main/fa_trademark.html")


def online_service(request):
    return render(request, "main/online-service.html")


def fa_online_service(request):
    return render(request, "main/fa_online-service.html")


def copyright_view(request):
    return render(request, "main/copyright.html")


def fa_copyright_view(request):
    return render(request, "main/copyright_fa.html")


def translation_view(request):
    return render(request, "main/translation.html")


def fa_translation_view(request):
    return render(request, "main/fa_translation.html")


def ipserver_view(request):
    return render(request, "main/ip-server.html")


def fa_ipserver_view(request):
    return render(request, "main/fa_ip-server.html")


def design_view(request):
    return render(request, "main/design.html")


def fa_design_view(request):
    return render(request, "main/fa_design.html")


def homepage_view(request):
    return render(request, "main/home.html")


def fa_homepage_view(request):
    return render(request, "main/fa_home.html")


def services_view(request):
    return render(request, "main/services.html")


def fa_services_view(request):
    return render(request, "main/fa_services.html")


def about_us_view(request):
    return render(request, "main/about_us.html")


def fa_about_us_view(request):
    return render(request, "main/fa_about_us.html")


def contact_us_view(request):
    return render(request, "main/contact_us.html")


def fa_contact_us_view(request):
    return render(request, "main/fa_contact_us.html")
