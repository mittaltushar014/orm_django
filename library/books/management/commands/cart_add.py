from django.core.management.base import BaseCommand, CommandError
from books.models import Cart
from django.contrib.auth.models import User
from django.conf import settings
from random import choice

class Command(BaseCommand):
    def cart_add(self):
        users = list(User.objects.all())
        for i in range(1,21): 
            Cart.objects.create(user=choice(users))

    def handle(self, *args, **options):
        self.cart_add()