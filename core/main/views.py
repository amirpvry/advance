from django.shortcuts import render


def home_view(request):
    return render(request, "main/index.html")


def about_view(request):
    return render(request, "main/about.html")


def trademark(request):
    return render(request, "main/trademark.html")


def online_service(request):
    return render(request, "main/online-service.html")


def copyright_view(request):
    return render(request, "main/copyright.html")


def translation_view(request):
    return render(request, "main/translation.html")


def ipserver_view(request):
    return render(request, "main/ip-server.html")


def design_view(request):
    return render(request, "main/design.html")


def fa_copyright_view(request):
    return render(request, "main/copyright_fa.html")


def homepage_view(request):
    return render(request, "main/home.html")


def services_view(request):
    return render(request, "main/services.html")


def about_us_view(request):
    return render(request, "main/about_us.html")


def contact_us_view(request):
    return render(request, "main/contact_us.html")
