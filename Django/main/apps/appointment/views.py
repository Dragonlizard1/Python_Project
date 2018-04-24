# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib import messages
from django.shortcuts import render, redirect, HttpResponse
from time import gmtime, strftime, strptime
import time
from datetime import date, datetime


from django.utils.crypto import get_random_string 
from .models import *
# Create your views here.
def index(request):
	
	return redirect("/main" )

def mainindex(request):
	
	return render(request, "appointment/index.html" )

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
	return redirect("/appointments")

def appointment(request):
	data = users.objects.get(id = request.session["id1"] )
	name = data.first_name + " " + data.last_name
	appoint3 = []

	appoint5 = appoint_list.objects.filter(appointment_id = request.session["id1"])
	appoint_today = appoint5.filter(date1 = date.today()) # today date

	appoint_other = appoint5.exclude(date1 = date.today()) # other day but format date correctly
	
	dateset = time.strftime("%B %d, %Y")
	if appoint_other:
		for element in appoint_other:
			print element.id
			appoint2 = {
			"id1" : element.id,
	        "task" : element.task,
	        "date1" : element.date1.strftime("%B %d, %Y"),
	        "time" : element.time,
	        "status" : element.status
			}
			appoint3.append(appoint2)

	content1 = {
		"name" : name, 
		"date1" : dateset,
		"appoint3" : appoint_today,
		"appoint5" : appoint3
	}
	return render(request, 'appointment/appointment.html', content1)

def process(request):
	print request.session["id1"]
	appoint_list.objects.appoint_create(request.POST, request.session["id1"])


	data = users.objects.get(id = request.session["id1"])
	name = data.first_name + " " + data.last_name
	return redirect("/appointments")

def update(request, appoint_id):
	data = appoint_list.objects.get(id = appoint_id)
	content1 ={
	"id1" : appoint_id,
	"task" : data.task,
	"date" : data.date1,
	"time" : data.time,
	}

	return render(request, "appointment/update.html", content1)

def update2(request, appoint_id):
	appoint_list.objects.appoint_update(request.POST, appoint_id)

	return redirect("/appointments")

def delete(request, appoint_id):
	appoint_list.objects.get(id = appoint_id).delete()

	return redirect("/appointments")

