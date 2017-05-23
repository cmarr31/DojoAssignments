from django.shortcuts import render, HttpResponse, redirect
import requests
from random import *
from .models import Product

word_site = "http://svnweb.freebsd.org/csrg/share/dict/words?view=co&content-type=text/plain"
response = requests.get(word_site)
WORDS = response.content.splitlines()
# Create your views here.
def index(request):
    products = Product.objects.all()
    context = {
        "products": products
    }
    return render(request, "index.html", context)

def new_product(request):
    x = randint(1, len(WORDS))
    product = Product.objects.create(name =WORDS[x], weight ="1lb", price = "649",cost = "500",category = "consumr elctrncs")
    products = Product.objects.all()
    print products

    return redirect("/")