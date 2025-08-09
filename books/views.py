from django.http import HttpResponse
from django.shortcuts import render
from .models import Booksvariety

# Create your views here.
def book_home(request):
    books = Booksvariety.objects.all()
    return render(request, 'books/all_books.html')