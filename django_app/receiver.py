from django.core.signals import request_finished
from django.dispatch import receiver
from django.db.models.signals import pre_save
from django_app.models import *


@receiver(pre_save, sender=Author)
def my_callback(sender, **kwargs):
    print("author has been created.")

