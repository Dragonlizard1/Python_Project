# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render, redirect, HttpResponse

from time import gmtime, strftime
from django.utils.crypto import get_random_string 
from .models import *


#@app.route('/')
def index(request):
	return redirect ("/courses")

#@app.route('/courses')
def mainindex(request):


	return render(request, 'Course/index.html', {"courses" : courses.objects.all()})

#@app.route('/users/<user_id>')
def show(request, user_id):

	return render(request,'Course/show.html', {"courses" : courses.objects.get(id = int(user_id))})

#@app.route('/users/create', methods=['POST'])
def process_new(request):

	
	class1 = courses.objects.create(name = request.POST['name'])
	class_descrip = info.objects.create(description = request.POST['description'], descrip = class1)
	
	
	return redirect('/courses')



#@app.route('/users/<user_id>/destroy')
def delete(request, user_id):



	content = {
	
	"courses" : courses.objects.get(id = int(user_id))
	}
	return render(request, 'Course/remove.html', content)


#@app.route('/destroy/<user_id>', methods=['POST'])
def delete2(request, user_id):

	class1 = courses.objects.get(id = int(user_id))
	class1.delete()

	return redirect('/')

