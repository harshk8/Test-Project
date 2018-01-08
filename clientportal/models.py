# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

from django.utils import timezone
import datetime
from django.contrib.auth.models import User


class UserProfile(models.Model):
	userdata = models.OneToOneField(User, on_delete=models.CASCADE)
	is_confirm = models.BooleanField(default='False')


class Client(models.Model):
	
	STATE_CHOICES = ((
		('AL', 'AL'),
		('AK', 'AK'),
		('AZ', 'AZ'),
		('AR', 'AR'),
		('CA', 'CA'),
		('CO', 'CO'),
		('CT', 'CT'),
		('DE', 'DE'),
		('FL', 'FL'),
		('GA', 'GA'),
		('HI', 'HI'),
		('ID', 'ID'),
		('IL', 'IL'),
		('IN', 'IN'),
		('IA', 'IA'),
		('KS', 'KS'),
		('KY', 'KY'),
		('LA', 'LA'),
		('ME', 'ME'),
		('MD', 'MD'),
		('MA', 'MA'),
		('MI', 'MI'),
		('MN', 'MN'),
		('MS', 'MS'),
		('MO', 'MO'),
		('MT', 'MT'),
		('NE', 'NE'),
		('NV', 'NV'),
		('NH', 'NH'),
		('NJ', 'NJ'),
		('NM', 'NM'),
		('NY', 'NY'),
		('NC', 'NC'),
		('ND', 'ND'),
		('OH', 'OH'),
		('OK', 'OK'),
		('OR', 'OR'),
		('PA', 'PA'),
		('RI', 'RI'),
		('SC', 'SC'),
		('SD', 'SD'),
		('TN', 'TN'),
		('TX', 'TX'),
		('UT', 'UT'),
		('VT', 'VT'),
		('VA', 'VA'),
		('WA', 'WA'),
		('WV', 'WV'),
		('WI', 'WI'),
		('WY', 'WY'),
	))

	PREFIX_CHOICES = ((
		('mr.', 'Mr.'),
		('ms.', 'Ms.', ),
		('mrs.', 'Mrs.'),
	))

	userprofile = models.OneToOneField(UserProfile, on_delete=models.CASCADE, default=None)
	prefix = models.CharField(max_length=10, choices=PREFIX_CHOICES)
	first_name = models.CharField(max_length=20)
	middle_name = models.CharField(max_length=20, blank=True, null=True,)
	last_name = models.CharField(max_length=20)
	address = models.CharField(max_length=100)
	city = models.CharField(max_length=100)
	state = models.CharField(max_length=10, choices=STATE_CHOICES) 
	zipcode = models.IntegerField(max_length=10)
	landline = models.IntegerField(max_length=15)
	cell = models.IntegerField(max_length=11)
	fax = models.CharField(max_length=20)


class Property(models.Model):
	client = models.ForeignKey(Client, on_delete=models.CASCADE)
	location = models.CharField(max_length=50, default='Indore')


class Retainer(models.Model):

	YEAR_CHOICES = ((
		(13, 2013),
		(14, 2014),
		(15, 2015),
		(16, 2016),
		(17, 2017),
	))
	properties = models.ForeignKey(Property, on_delete=models.CASCADE)
	work_year = models.IntegerField(default=2017, choices=YEAR_CHOICES)
	sign = models.CharField(max_length=20)
	verified = models.BooleanField(default=False)