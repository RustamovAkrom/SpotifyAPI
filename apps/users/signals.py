import os

from django.db.models.signals import post_save
from django.dispatch import receiver
from django.template.loader import render_to_string
from django.utils.html import strip_tags

from celery import shared_task

from .models import User, UserProfile
from .utils import generate_token
from .tasks import send_activation_email


@shared_task
@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):

    if created:
        UserProfile.objects.create(user=instance, email=instance.email)

        instance.token = generate_token()
        instance.save()

        context = {
            "username": instance.username,
            "email": instance.email,
            "activation_link": f"http://localhost:8000/api/v1/users/user-activation/{instance.token}",
        }
        message = render_to_string("index.html", context=context)

        try:
            send_activation_email(
                subject=f"Spotify: {instance.username} your activation link",
                message=strip_tags(message),
                from_email=os.getenv("EMAIL_HOST_USER"),
                recipient_list=[instance.email],
            )

        except Exception as e:
            print(e)
