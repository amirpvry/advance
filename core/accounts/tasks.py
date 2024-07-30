from celery import shared_task
from time import sleep

@shared_task
def SendEmail():
    sleep(10)
    print("Sending email 10")
    