from django.contrib.auth import get_user_model
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    def handle(self, *args, **options):
        User = get_user_model()
        options.setdefault("is_active", True)
        self.create_superuser(User, "Akromjon", "akromjonrustamov56@gmail.com", "2007")

    def create_superuser(self, User, username, email, password):
        if not User.objects.filter(username=username).exists():
            user = User.objects.create_superuser(username, email, password)
            user.is_active = True
            user.save()
            self.stdout.write(
                self.style.SUCCESS(f"Superuser {username} created successfully.")
            )
        else:
            self.stdout.write(self.style.ERROR(f"Superuser {username} already exists."))
