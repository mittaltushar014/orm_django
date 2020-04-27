from django.core.management.base import BaseCommand, CommandError
from books.models import Book, Category, BookCategory
from random import sample

class Command(BaseCommand):
    def book_categories_add(self):
        books = list(Book.objects.all())
        categories = list(Category.objects.all())
        for book in books:
            book_categories = sample(categories, 3)
            for category in book_categories:
                BookCategory.objects.create(book=book, category=category)

    def handle(self, *args, **options):
        self.book_categories_add()