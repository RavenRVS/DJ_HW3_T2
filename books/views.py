from django.core.paginator import Paginator
from django.shortcuts import render

from books.models import Book


def books_view(request):
    template = 'books/books_list.html'
    books = Book.objects.all()
    context = {
        'books': books
    }
    return render(request, template, context)


def books_by_date(request, pub_date):
    template = 'books/books_by_date.html'
    books_for_this_date = Book.objects.filter(pub_date=pub_date)
    all_dates = Book.objects.values_list("pub_date", flat=True).distinct()
    sorted_list_dates = sorted([date for date in all_dates])
    page_number = None
    prev_date = None
    next_date = None
    i = 0
    paginator = Paginator(sorted_list_dates, 1)
    for date in paginator.object_list:
        if str(date) == pub_date:
            page_number = i + 1
            if i > 0:
                prev_date = str(paginator.object_list[i - 1])
            if i < len(paginator.object_list) - 1:
                next_date = str(paginator.object_list[i + 1])
            break
        else:
            i += 1
    page = paginator.get_page(page_number)

    context = {
        'books': books_for_this_date,
        'paginator': paginator,
        'pub_date': pub_date,
        'page': page,
        'prev_date': prev_date,
        'next_date': next_date
    }
    return render(request, template, context)
