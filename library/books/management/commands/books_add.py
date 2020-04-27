from django.core.management.base import BaseCommand, CommandError
from books.models import Book
from random import randint

class Command(BaseCommand):
    def books_add(self):
        for i in range(1,41): 
            Book.objects.create(title="b"+str(i), price=randint(1,100))

    def handle(self, *args, **options):
        self.books_add()