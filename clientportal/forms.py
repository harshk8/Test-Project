from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth.tokens import default_token_generator
from django.contrib.sites.shortcuts import get_current_site
from django.core.mail import EmailMultiAlternatives
from django.template import loader
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode
from django.utils.text import capfirst
from django.utils.translation import ugettext, ugettext_lazy as _
from clientportal.models import Client, Property, Retainer
from django.contrib.auth import authenticate


class UserForm(forms.ModelForm):
		
	class Meta:
		model = User
		fields = ('username', 'email', 'password')


class ClientForm(forms.ModelForm):

	class Meta:
		model = Client
		fields = ('prefix', 'first_name', 'middle_name', 'last_name', 'address', 'city', 'state', 'zipcode', 'landline', 'cell', 'fax')


class PropertyForm(forms.ModelForm):

	class Meta:
		model = Property
		fields = ('location',)


class RetainerForm(forms.ModelForm):
	
	class Meta:
		model = Retainer
		fields = ('work_year',)

