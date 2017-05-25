# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render, redirect, HttpResponse
from django.contrib.messages import get_messages
from django.contrib import messages
from django.db.models import Count
from .models import User, Book, Author, Review

def index(request):
    context = {
        'messages':get_messages(request)
    }
    return render(request, "my_app/index.html", context)

def register(request):
    if request.method == "POST":
        post_data = {
            'full_name':request.POST['full_name'],
            'alias':request.POST['alias'],
            'email':request.POST['email'],
            'password':request.POST['password'],
            'confirm_password':request.POST['confirm_password']
        }
        register_result = User.objects.register(post_data)
        print "*"*100
        print register_result
        if register_result['result'] == "failed_validation":
            if 'messages' in register_result.keys():
                for message in register_result['messages']:
                    messages.error(request, message)
            return redirect('/')
        else:
            if 'user' in register_result.keys():
                request.session['current_user'] = register_result['user'].id
                if 'messages' in register_result.keys():
                    for message in register_result['messages']:
                        messages.success(request, message)
            else:
                messages.error(request, "Something went wrong")
                return redirect('/')
            return redirect('/landing_page')
    return redirect('/')

def landing_page(request):
    #response = "welcome to the landing page!"
    #return HttpResponse(response)
    context = {
        "messages":get_messages(request),
        "reviews":Review.objects.all().order_by('-created_at')[:3],
        "books":Book.objects.all().order_by('title')
    }
    if "current_user" in request.session.keys():
        context['user'] = User.objects.get(pk=request.session['current_user'])
    return render(request, "my_app/landing_page.html", context)

def login(request):
    if request.method == "POST":
        post_data = {
            'email':request.POST['email'],
            'password':request.POST['password']
        }
        login_result = User.objects.login(post_data)
        print login_result
        if login_result['result'] == "failed_authentication":
            print "login result returned failed authentication"
            if 'messages' in login_result.keys():
                for message in login_result['messages']:
                    messages.error(request, message)
            return redirect('/')
        else:
            if 'user' in login_result.keys():
                request.session['current_user'] = login_result['user'].id
                # if 'messages' in login_result.keys():
                #     for message in login_result['messages']:
                #         messages.success(request, message)
            else:
                messages.error(request, "Something went wrong")
                return redirect('/')
            return redirect('/landing_page')

def logout(request):
    request.session.clear()
    messages.success(request, "Successfully logged out")
    return redirect('/')

def show_add_book_page(request):
    context = {
        "messages":get_messages(request),
        "authors":Author.objects.all
    }
    if "current_user" in request.session.keys():
        context['user'] = User.objects.get(pk=request.session['current_user'])
    return render(request, "my_app/add_book.html", context)

def process_add_book(request):
    if request.method == "POST":
        completed_form = True
        title = request.POST['title']
        if len(title) < 2:
            completed_form = False
            messages.error(request, "Title is required")
            print "Title is required"
        author = ""
        if request.POST['author-select'] != "":
            author = request.POST['author-select']
            print "found author in dropdown menu"
            print author
        else:
            author = request.POST['new-author']
            print "found new author"
            print author

            if author:
                try:
                    found = Author.objects.get(full_name=author)
                    print "Author already exists"
                    author = found.id
                except:
                    Author.objects.create(full_name=author)
                    author = Author.objects.get(full_name=author).id
                    messages.success(request, "Created new Author")
                    print "Created new author"
        if not author:
            completed_form = False
            messages.error(request, "Author is required")
            print "Author is required"
        content = request.POST['review']
        if len(content) < 2:
            completed_form = False
            messages.error(request, "Review is too short")
            print "Review is too short"
        stars = request.POST['rating']
        print "Title:", title
        print "Author ID:", author
        print "Review:", content
        print "Rating:", stars
        if completed_form:
            Book.objects.create(title=title, author=Author.objects.get(pk=int(author)))
            print "Created new book"
            book = Book.objects.get(title=title)
            user = User.objects.get(pk=request.session['current_user'])
            Review.objects.create(content=content, stars=stars, book=book, user=user)
            print "Added new review"
        else:
            messages.error(request, "please try again")
    return redirect('/new_book')

def show_book_page(request, book_id):
    book = Book.objects.get(pk=book_id)
    context = {
        "book":book,
        "reviews":Review.objects.filter(book=book)
    }
    return render(request, "my_app/book_page.html", context)

def show_user_profile(request, user_id):
    user = User.objects.get(pk=user_id)
    context = {
        "user":user,
        "reviews":Review.objects.filter(user=user),
        "reviewed_books":Book.objects.filter(reviews__user=user).distinct()
    }
    context['num_reviews'] = len(context['reviews'])
    return render(request, "my_app/user_profile.html", context)

def add_review(request, book_id):
    if request.method == "POST":
        content = request.POST['content']
        stars = request.POST['rating']
        user = User.objects.get(pk=request.session['current_user'])
        book = Book.objects.get(pk=book_id)
        Review.objects.create(content=content, stars=stars, user=user, book=book)
    return redirect('/book/' + book_id)

def delete_review(request, review_id):
    review = Review.objects.get(pk=review_id)
    book_id = review.book.id
    review.delete()
    return redirect('/book/' + str(book_id))

def add_to_my_favorites(request, book_id):
    user = User.objects.get(pk=request.session['current_user'])
    book = Book.objects.get(pk=book_id)
    user.books.add(book)
    return redirect('/landing_page')

# redirect(reverse("home"))