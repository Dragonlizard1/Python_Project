# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib import messages
from django.shortcuts import render, redirect, HttpResponse
from time import gmtime, strftime, strptime
from datetime import date, datetime


from django.utils.crypto import get_random_string 
from .models import *

def index(request):
	
	return redirect("/main" )

def mainindex(request):
	
	return render(request, "book_reviewer/index.html" )

def logout(request):
	request.session.clear()
	return redirect("/main" )

def register(request):
	errors = users.objects.reg_validator(request.POST)
	if len(errors):
		for tag, error in errors.iteritems():
			messages.error(request, error, extra_tags=tag)
		return redirect("/main")
	else:
		users.objects.data_create(request.POST)

	
	return redirect('/main')

def login(request):
	errors = users.objects.login_validator(request.POST)
	if len(errors):
		for tag, error in errors.iteritems():
			messages.error(request, error, extra_tags=tag)
		return redirect("/main")
	data = users.objects.get(email_address = request.POST['email'])
	request.session["id1"] = data.id
	return redirect("/books")

def books(request):
	user1 = users.objects.get(id = request.session["id1"])
	booklist = reviews.objects.all().values("rev_rev__title","rev_rev__id",
	"comment", "created_at", "rev_rev__rating", "review__first_name", "review_id")
	#booklist = booklist[0].book_rev.all()
	#newbook = booklist.rev_rev.all()

	#booklist = booklist.rev_rev.all()
	


	list1 = []
	list2 = []
	i = 1
	if booklist:
		for element in reversed(booklist):
			starnum = ""
			if i <= 3:
				for index in range(0,5):
					if index < element["rev_rev__rating"]:
						starnum += "y"
					else:
						starnum += "x"
				element["starnum"] = starnum
				list1.append(element)
			else:
				
				for index in range(0,5):
					if index < element["rev_rev__rating"]:
						starnum += "y"
					else:
						starnum += "x"
				element["starnum"] = starnum
				list2.append(element)
			i +=1



	
	
	
	content1 = {
		"name" : user1.first_name,
		"booklist" : list1,
		"booklist1" : list2

	}


	return render(request, "book_reviewer/books.html", content1)

def add(request):


	return render(request, "book_reviewer/add_book_rev.html")

def add2(request):
	
	book_title.objects.add_create(request.POST,  request.session["id1"])



	return redirect("/books")

def book_review(request, book_id):
	review = reviews.objects.all().values("rev_rev__title","rev_rev__id",
	"comment", "created_at", "rev_rev__rating", "review__first_name", "review_id")
	review = review.filter(rev_rev__id = book_id)
	book = book_title.objects.get(id = book_id)

	list1 = []
	for element in review:
		starnum = ""
	
		for index in range(0,5):
			if index < book.rating:
				starnum += "y"
			else:
				starnum += "x"
		element["starnum"] = starnum
		list1.append(element)


	content1 = {"review": list1,
	"book":book,


	}
	return render(request, "book_reviewer/books_review.html", content1)

def add_review(request, book_id):
	book_title.objects.add_review(request.POST,  request.session["id1"], book_id)

	return redirect("/book_review/" + book_id)


