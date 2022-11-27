import json

from django.core.management.base import BaseCommand
from books.models import Book


class Command(BaseCommand):

    def handle(self, *args, **options):
        with open('fixtures/books.json', 'r', encoding='utf-8') as file:
            books = json.load(file)

        for book in books:
            Book.objects.create(name=book['fields']['name'],
                                author=book['fields']['author'],
                                pub_date=book['fields']['pub_date']
                                )
