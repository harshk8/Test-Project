# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from clientportal.models import Client, UserProfile, Property, Retainer

# from .models import User, Client


class UserProfileAdmin(admin.ModelAdmin):
	list_display = ['id', 'is_confirm']
admin.site.register(UserProfile, UserProfileAdmin)


class ClientAdmin(admin.ModelAdmin):
	list_display = ['prefix', 'first_name', 'middle_name', 'last_name', 'address', 'city', 'state', 'zipcode', 'cell', 'fax']
admin.site.register(Client, ClientAdmin)


class PropertyAdmin(admin.ModelAdmin):
	list_display = ['location']
admin.site.register(Property, PropertyAdmin)


class RetainerAdmin(admin.ModelAdmin):
	list_display = ['work_year', 'sign', 'verified' ]
admin.site.register(Retainer, RetainerAdmin)
