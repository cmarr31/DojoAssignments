# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render, HttpResponse, redirect
from .models import Book

def index(request):
    all_books = Book.objects.all()
    for book in all_books:
        print book
    context = {
        "books":all_books
    }
    return render(request, 'index.html', context)

def create(request):
    if request.method == "POST":
        data={
            "title":request.POST["title"],
            "author":request.POST["author"],
            "category":request.POST["category"],
            "published_date":request.POST["published_date"]
        }
        Book.objects.validate(data)
    return redirect('/')
'''
def show_delete_confirmation(request, book_id):
    book = Book.objects.get(pk=book_id)
    context = {
        "book":book
    }
    return render(request, "confirmation_page.html", context)

def delete_book(request, book_id):
    Book.objects.get(pk=book_id).delete()
    return redirect('/')
'''