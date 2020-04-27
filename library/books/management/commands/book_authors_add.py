from django.core.management.base import BaseCommand, CommandError
from books.models import Book, BookAuthor
from django.contrib.auth.models import User
from django.conf import settings
from random import sample

class Command(BaseCommand):
    def book_authors_add(self):
        books = list(Book.objects.all())
        users = list(User.objects.all())
        for book in books:
            book_users = sample(users, 2)
            for user in book_users:
                BookAuthor.objects.create(book=book, author=user)

    def handle(self, *args, **options):
        self.book_authors_add()