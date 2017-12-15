from django.shortcuts import render
from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse

from .models import Author, Book, RentalStatus

def index(request):
    # books = Book.objects.all()
    checked_in_books = Book.objects.filter(checked_in=True)
    checked_out_books = Book.objects.filter(checked_in=False)
    history = RentalStatus.objects.all()
    return render(request, 'library/index.html', {'checked_in_books': checked_in_books,
                                                  'checked_out_books': checked_out_books,
                                                  'history': history})


def checkout(request):
    print(request.POST)
    book_id = request.POST['id']
    book = get_object_or_404(Book, pk=book_id)
    book.checked_in = False
    book.save()
    logStatus(book, False, request.POST['user'])

    return HttpResponseRedirect(reverse('library:index'))


def checkin(request):
    book_id = request.POST['id']
    book = get_object_or_404(Book, pk=book_id)
    book.checked_in = True
    book.save()
    logStatus(book, True, request.POST['user'])

    return HttpResponseRedirect(reverse('library:index'))

def logStatus(book, checked_in, user):
    status = RentalStatus(book=book, checked_in=checked_in, user=user)
    status.save()


