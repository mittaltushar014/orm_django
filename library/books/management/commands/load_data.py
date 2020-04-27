from django.core.management.base import BaseCommand, CommandError
from django.contrib.auth.models import User
from random import choices, choice, randint, sample
from books.models import *

class Command(BaseCommand):
    
    def users_add(self):
        for i in range(1,11): 
            user=User.objects.create_user("u"+str(i), password="tm123")
            user.save()

    def books_add(self):
        for i in range(1,41): 
            Book.objects.create(title="b"+str(i), price=randint(1,100))   

    def categories_add(self):
        for i in range(1,11): 
            Category.objects.create(name="c"+str(i))   

    def book_categories_add(self):
        books = list(Book.objects.all())
        categories = list(Category.objects.all())
        for book in books:
            book_categories = sample(categories, 3)
            for category in book_categories:
                BookCategory.objects.create(book=book, category=category) 

    def book_authors_add(self):
        books = list(Book.objects.all())
        users = list(User.objects.all())
        for book in books:
            book_users = sample(users, 2)
            for user in book_users:
                BookAuthor.objects.create(book=book, author=user)  

    def cart_add(self):
        users = list(User.objects.all())
        for i in range(1,21): 
            Cart.objects.create(user=choice(users))    

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
        self.users_add()
        self.books_add()
        self.categories_add()
        self.book_categories_add()
        self.book_authors_add()
        self.cart_add()
        self.cart_item_add()
        