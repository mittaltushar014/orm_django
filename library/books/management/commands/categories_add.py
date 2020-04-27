from django.core.management.base import BaseCommand, CommandError
from books.models import Category

class Command(BaseCommand):
    def categories_add(self):
        for i in range(1,11): 
            Category.objects.create(name="c"+str(i))

    def handle(self, *args, **options):
        self.categories_add()