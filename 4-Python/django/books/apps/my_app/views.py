from django.shortcuts import render, HttpResponse, redirect
import requests
from random import *
from .models import Book
# word_site = "http://svnweb.freebsd.org/csrg/share/dict/words?view=co&content-type=text/plain"
# response = requests.get(word_site)
# WORDS = response.content.splitlines()
# title =WORDS[x]
def index(request):
	return render(request, "index.html")

def new_book(request):
    x = randint(1, len(WORDS))
    book = Book.objects.create(title ="my book #"+str(x), author ="mau rua", published_date = "2017",category = "novel",in_print = "true")
    books = Book.objects.all()
    return redirect("/")