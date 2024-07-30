from django.http import HttpResponse
import time
from .tasks import SendEmail


def send_email(request):
    SendEmail.delay()
    return HttpResponse("<h1> sending email</h1>")
