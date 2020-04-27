from django.core.management.base import BaseCommand, CommandError
from django.contrib.auth.models import User

class Command(BaseCommand):
    
    def users_add(self):
        for i in range(1,11): 
            user=User.objects.create_user("u"+str(i), password="tm123")
            user.save()

    def handle(self, *args, **options):
        self.users_add()