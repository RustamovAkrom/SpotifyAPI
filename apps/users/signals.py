from django.db.models.signals import post_save
from django.dispatch import receiver
from apps.users.models import User, UserProfile

from dotenv import load_dotenv

load_dotenv()
import os

from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.utils.html import strip_tags

from .utils import generate_token
<<<<<<< HEAD
from celery import shared_task
=======
from config.celery import app

>>>>>>> 8ba28da (update dir in push)

from django.views.decorators.cache import cache_page
from django.utils.decorators import method_decorator


@method_decorator(cache_page(60 * 10))
<<<<<<< HEAD
@shared_task()
=======
@app.task(bind = True)
>>>>>>> 8ba28da (update dir in push)
@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    email_host_user = os.getenv("EMAIL_HOST_USER")

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
        # send email activation account
        send_mail(
            subject=f"Spotify: {instance.username} your activation link",
            message=strip_tags(message),
            from_email=email_host_user,
            recipient_list=[instance.profiles.email],
        )
