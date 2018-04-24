# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from time import gmtime, strftime, strptime
from datetime import date, datetime
import re
import bcrypt
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]$')
NAME_REGEX = re.compile(r'^[a-zA-Z]$')
PASSWORD_REGEX = re.compile(r'^[a-zA-Z]$')

class checkManager(models.Manager):
	def reg_validator(self, postData):
		errors = {}
		for element, data in postData.iteritems():
			print data
		if len(postData['f_name']) <= 2:
			errors["first_name"] = "First Name should be more than 2 characters"

		if NAME_REGEX.match(postData['f_name']):
			errors["first_name"] = "First Name should be characters only"

		if len(postData['l_name']) <= 2:
			errors["last_name"] = "Last Name should be more than 2 characters"

		if NAME_REGEX.match(postData['l_name']):
		
			errors["last_name"] = "Last Name should be characters only"

		if EMAIL_REGEX.match(postData['email']):
			errors["email"] = "Email should be format correctly"

		if PASSWORD_REGEX.match(postData['password']):
			errors["password"] = "Password should be characters only"

		if len(postData['password']) <= 4:
			errors["password"] = "Password should be more than 4 characters"
		
		return errors

	def login_validator(self, postData):
		errors = {}
		if EMAIL_REGEX.match(postData['email']):
			errors["email"] = "Email should be format correctly"
		if PASSWORD_REGEX.match(postData['password']):
			errors["password"] = "Password should be characters only"
		if len(postData['password']) <= 4:
			errors["password"] = "Password should be more than 4 characters"
		
		if len(errors):
			return errors

		print postData["email"]
		data1 = users.objects.get(email_address = postData["email"])
	
		if postData["email"] != data1.email_address:
			errors["email"] = "Email is incorrect"
		else:
			userpass = users.objects.get(email_address = postData["email"]).password
			if bcrypt.checkpw(postData["password"].encode(), userpass.encode()):
				return errors
			else:
				errors["password"] = "password is incorrect"

		return errors

	def simple_validator(self, postData):
		errors = {}
		if len(postData['item']) == "":
			errors["item"] = "No empty entries."
		if len(postData['item']) <= 3:
			errors["item"] = "Need to be more than 3 character long."

		return errors

	def data_create(self, postData):
		hash1 = bcrypt.hashpw(postData["password"].encode(), bcrypt.gensalt())
		users.objects.create(first_name = postData["f_name"],
			last_name = postData["l_name"],
			email_address = postData["email"],
			password = hash1,
			hire = postData["hired"]
			)
		
		return

	def addwish(self,postData, userid):
		user = users.objects.get(id = userid)
		wishlist.objects.create(item = postData["item"], name1 = user.first_name, wish = user)

		return

	def addfriend(self, itemid, userid):
		wishadd1 = wishlist.objects.get(id = itemid)
		user = users.objects.get(id = userid)
		wishlist.objects.create(item = wishadd1.item, name1 = wishadd1.name1, wish = user)


		return


class users(models.Model):
	first_name = models.CharField(max_length = 255)
	last_name = models.CharField(max_length = 255)
	email_address = models.CharField(max_length = 255)
	password = models.CharField(max_length = 255)
	hire = models.DateTimeField()
	updated_at =  models.DateTimeField(auto_now = True)
	created_at = models.DateTimeField(auto_now_add = True)
	objects = checkManager()

class wishlist(models.Model):
	item = models.CharField(max_length = 255)
	wish = models.ForeignKey(users, related_name="wishs")
	name1 = models.CharField(max_length = 255)
	created_at = models.DateTimeField(auto_now_add = True)


