from django.core.management import BaseCommand

from users.models import User


class Command(BaseCommand):
    def handle(self, *args, **options):
        user = User.objects.create(
            email="protos@chaos.inf",
            first_name="Alex",
            last_name="Merser",
            is_active=True,
            is_staff=True,
            is_superuser=True
        )
        user.set_password("7931")
        user.save()
