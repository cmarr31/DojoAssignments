from django.shortcuts import render, HttpResponse, redirect
import requests
from random import *
from .models import Book
# word_site = "http://svnweb.freebsd.org/csrg/share/dict/words?view=co&content-type=text/plain"
# response = requests.get(word_site)
# WORDS = response.content.splitlines()
# title =WORDS[x]
def index(request):
	books = Book.objects.all()
	print books
	context = {
		"books": books
	}
	return render(request, "index.html", context)

def new_book(request):
	# x = randint(1, len(WORDS))
	x = randint(1, 150)
	book = Book.objects.create(title ="my book #"+str(x), author ="mau rua", published_date = "2017",category = "novel",in_print = "True")
	print book
	books = Book.objects.all()
	print books
	return redirect("/")