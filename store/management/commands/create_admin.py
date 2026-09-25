from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model

class Command(BaseCommand):
    help = 'Automatically creates a default admin superuser if it does not exist'

    def handle(self, *args, **options):
        User = get_user_model()
        if not User.objects.filter(username='admin').exists():
            User.objects.create_superuser('admin', 'admin@example.com', 'AmyraAdmin@123')
            self.stdout.write(self.style.SUCCESS('Successfully created default admin user: admin / AmyraAdmin@123'))
        else:
            self.stdout.write(self.style.SUCCESS('Admin user already exists.'))