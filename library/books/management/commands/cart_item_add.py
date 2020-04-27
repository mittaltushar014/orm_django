from django.core.management.base import BaseCommand, CommandError
from books.models import Book, Cart, CartItem
from random import choices

class Command(BaseCommand):
    def cart_item_add(self):
        cart = list(Cart.objects.all())
        books = list(Book.objects.all())
        for i in cart:
            cart_items = choices(books,k=3)
            unique_books = set(cart_items)
            book_count = {book:cart_items.count(book) for book in unique_books}
            for book in book_count:
                CartItem.objects.create(cart=i, book=book, quantity=book_count[book])

    def handle(self, *args, **options):
        self.cart_item_add()