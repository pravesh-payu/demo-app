from django.core.management.base import BaseCommand, CommandError


from UserApp.models import User


class Command(BaseCommand):
    help = "Post count update in user"

    def handle(self, *args, **options):
        return User.objects.post_count_update()
