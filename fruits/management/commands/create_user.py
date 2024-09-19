from django.core.management import BaseCommand

from users.models import User
from django.db.utils import IntegrityError


class Command(BaseCommand):

    def handle(self, *args, **options):
        # Create user
        params = dict(username='test', email='test@example.com', password='qwerty')
        user, user_status = User.objects.get_or_create(**params)
        # if user_status:
        #     user.is_staff = True
        #     user.is_superuser = True
        #     user.save()
        print([f'User has already exists.', 'User was created successfully.'][user_status])
