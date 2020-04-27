from django.contrib import admin
from .models import Book, Category, BookCategory, BookAuthor, Cart, CartItem

admin.site.register(Book)
admin.site.register(Category)
admin.site.register(BookCategory)
admin.site.register(BookAuthor)
admin.site.register(Cart)
admin.site.register(CartItem)
