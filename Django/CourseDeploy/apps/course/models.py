# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class courses(models.Model):
	name = models.CharField(max_length = 255)	
	created_at = models.DateTimeField(auto_now_add = True)
	updated_at = models.DateTimeField(auto_now = True)

class info(models.Model):
	descrip = models.OneToOneField(courses, related_name="descrips")
	description = models.TextField("none")
	comment = models.TextField("none")