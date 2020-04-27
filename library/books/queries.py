from .models import Book, Category, BookCategory, BookAuthor, Cart, CartItem
from django.contrib.auth.models import User
from django.db.models import Sum, Count, Max

import logging 
l = logging.getLogger('django.db.backends') 
l.setLevel(logging.DEBUG) 
l.addHandler(logging.StreamHandler())

def book_fetch_single(id):
    book = Book.objects.get(id=id)
    return book

def book_fetch_multiple(id_list):
    books = Book.objects.filter(id__in=(id_list))
    return books

def book_fetch_single_category(category):
    book_single_category = [bookcategory.book for bookcategory in BookCategory.objects.select_related('book').filter(category__name=category)]
    return book_single_category

def book_single_category_count(category):
    single_category_count = BookCategory.objects.filter(category__name=category).count()
    return single_category_count

def book_author_most():
    most_books_author = User.objects.get(id=BookAuthor.objects.values('author__id').annotate(Count('book_id')).order_by('-book_id__count')[0]["author__id"]).username
    return most_books_author

def book_total_price():
    price_total = Book.objects.all().aggregate(Sum('price'))
    return price_total

def book_maximum_cost():
    maximum_cost_book = Book.objects.filter(price=Book.objects.all().aggregate(Max('price'))["price__max"])
    return maximum_cost_book

def book_price_more_than(cost):
    price_more_than = Book.objects.filter(price__gt=cost).order_by('-price')
    return price_more_than

def book_delete(id):
    return Book.objects.get(id=id).delete()

def fetch_cart_items_with_related_books(id):
    cart_items_and_related_books = [cart_item.book for cart_item in CartItem.objects.select_related('book').filter(cart__id=id)]
    return cart_items_and_related_books
