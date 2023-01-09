from django.shortcuts import render, redirect, reverse
from django.views.decorators.http import require_POST, require_GET
from .models import Book
from random import randint
from faker import Faker
import math


@require_POST
def insert_books(request):
    faker = Faker()
    count = int(request.POST.get('count', 10))
    for i in range(count):
        Book.objects.create(name=faker.sentence(nb_words=3).replace('.', ''),
                            author=faker.name(),
                            year=randint(1904, 2023),
                            isbn=faker.isbn10(),
                            created_at=faker.date_this_decade())
    return redirect(reverse('list_books'))


@require_GET
def list_books(request):
    page = int(request.GET.get('page', 1))
    per_page = int(request.GET.get('limit', 25))
    total = Book.objects.count()

    offset = (page - 1) * per_page
    pages = int(math.ceil(total / per_page))

    books_list = Book.objects.all().order_by('-created_at')
    books_list = books_list[offset:offset+per_page]
    context = {'books': books_list, 'count': total,
               'page': page, 'per_page': per_page,
               'pages': pages}
    return render(request, 'books/list.html', context)
