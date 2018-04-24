# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import messages
from django.shortcuts import render, redirect, HttpResponse
from time import gmtime, strftime, strptime
from datetime import date, datetime

from .models import *

def index(request):
	
	return redirect("/main" )

def mainindex(request):
	
	return render(request, "wish/index.html" )

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
	return redirect("/dashboard")

def logout(request):
	request.session.clear()
	return redirect("/main" )

def dashboard(request):
	data = users.objects.get(id = request.session["id1"] )
	name = data.first_name
	wishlist1 = wishlist.objects.filter(wish_id = request.session["id1"])
	#wishlist2 = wishlist.objects.friend.all()
	list1 = []
	for element in wishlist1:
		list1.append(element.item)

	friendlist = wishlist.objects.exclude(item__in = list1)
	


	content1 = {
		"name" : name, 
	# 	"date1" : dateset,
	 	"wishlist" : wishlist1,
	 	"friendlist" : friendlist
	}

	print wishlist1
	return render(request, 'wish/dashboard.html', content1)

def additem(request, user_id):


	return render(request, "wish/additem.html")

def additem2(request, user_id):

	

	errors = users.objects.simple_validator(request.POST)
	if len(errors):
		for tag, error in errors.iteritems():
			messages.error(request, error, extra_tags=tag)
		return render(request, "wish/additem.html")

	users.objects.addwish(request.POST, user_id)

	return redirect("/dashboard")

def addtofriend(request, item_id):
	users.objects.addfriend(item_id, request.session["id1"])

	return redirect("/dashboard")

def show(request, item_id):

	userlist = wishlist.objects.get(id = item_id)

	list2 = wishlist.objects.filter(item = userlist.item)



	content1 = {
		"item" : userlist.item,
	 	"userlist" : list2,
	 
	 
	}

	return render(request, "wish/wishshow.html", content1)

def delete(request, item_id):
	wishlist.objects.get(id = item_id).delete()


	return redirect("/dashboard")




# def process(request):
# 	print request.session["id1"]
# 	appoint_list.objects.appoint_create(request.POST, request.session["id1"])


# 	data = users.objects.get(id = request.session["id1"])
# 	name = data.first_name + " " + data.last_name
# 	return redirect("/appointments")


