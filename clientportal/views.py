from django.shortcuts import render, redirect
from django.contrib.auth import authenticate
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as django_logout
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.core.exceptions import ValidationError
from django.contrib import messages
from django.contrib.sites.shortcuts import get_current_site
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode
from django.template.loader import render_to_string
from django.core.mail import EmailMessage
from django.utils.encoding import force_text
from django.utils.http import urlsafe_base64_decode
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import password_reset, password_reset_confirm
from django.urls import reverse
from django.contrib.auth import get_user_model
from django.conf import settings
from django.contrib.auth.models import Group
from django.contrib.auth.models import User
from django.core.mail import send_mail

import urllib
import urllib2
import json

from .models import UserProfile, Client, Property, Retainer
from clientportal.forms import UserForm, ClientForm, PropertyForm, RetainerForm
from .tokens import account_activation_token


@login_required(login_url="/user/login/")
def account_activate_token(request, user):

	current_site = get_current_site(request)
	subject = 'Activate Your User Account'
	message = render_to_string('clientportal/account_activation_email.html', {
		'user': user,
		'domain': current_site.domain,
		'uid': urlsafe_base64_encode(force_bytes(user.pk)),
		'token': account_activation_token.make_token(user)
		})

	to_email = user.email
	send_mail(subject, message, '', [to_email], fail_silently=False	)
	return None

@login_required(login_url="/user/login/")
def reset_password_token(request):
	user = User.objects.get(email=request.POST['email'])
	current_site = get_current_site(request)
	subject = 'Activate Your User Account'
	message = render_to_string('clientportal/reset_password_email.html', {
		'user': user,
		'domain': current_site.domain,
		'uid': urlsafe_base64_encode(force_bytes(user.pk)),
		'token': account_activation_token.make_token(user)
	})

	to_email = request.POST['email']

	send_mail(subject, message, '', [to_email], fail_silently=False	)
	return None


def signup(request):

	if request.method == 'POST':
		form = UserForm(request.POST)

		if form.is_valid():
			useremail = form.cleaned_data['email']
			password = form.cleaned_data['password']

			if User.objects.filter(email=useremail).exists():
				messages.error(request, 'Email Already Exist!')
				return redirect('/')

			else:
				if recaptcha(request):
					user= form.save()
					user.set_password(password)
					user.save()

					UserProfile.objects.create(userdata=user, is_confirm="False")
					auth_login(request, user)

					account_activate_token(request, user)
					
					messages.success(request, "<center> Confirm Your Account.<center> <br>. Please check your inbox (and your spam folder) you should have received an email with a confirmation link.")
					return HttpResponseRedirect('/user/un_confirm/')

				else:
					messages.error(request, 'Invalid reCAPTCHA. Please try again.')
					return redirect('/')

		else:
			messages.error(request, 'Entered data not satisfied')
			return redirect('/')

	form = UserForm()
	return render(request, 'clientportal/signup.html', {"form": form})


def recaptcha(request):
	''' Begin reCAPTCHA validation '''
	recaptcha_response = request.POST.get('g-recaptcha-response')
	url = 'https://www.google.com/recaptcha/api/siteverify'
	values = {
		'secret': settings.GOOGLE_RECAPTCHA_SECRET_KEY,
		'response': recaptcha_response
	}
	data = urllib.urlencode(values)
	req = urllib2.Request(url, data)
	response = urllib2.urlopen(req)
	result = json.load(response)
	''' End reCAPTCHA validation '''
	return result


def unconfirm(request):
	return render(request, 'clientportal/unconfirm.html')


def resend_token(request):
	''' Again token Generation on click --RESEND--'''
	user_inst = request.user
	account_activate_token(request, user_inst)
	messages.error(request, 'Link again send on your E-mail. Please Verify and activate your account.')
	return render(request, 'clientportal/unconfirm.html')


def account_activate(request, uidb64, token):
	try:
		uid = force_text(urlsafe_base64_decode(uidb64))
		user = User.objects.get(pk=uid)

	except (TypeError, ValueError, OverflowError, User.DoesNotExist):
		user = None

	if user is not None and account_activation_token.check_token(user, token):
		uemail = user.email
		
		auth_login(request, user)
		userprofile = UserProfile.objects.get(userdata=user)
		userprofile.is_confirm = True
		userprofile.save()

		return redirect('/dashboard/')

	else:
		return HttpResponse('Fail to activate your account.')


def reset_activate(request, uidb64, token):
	try:
		uid = force_text(urlsafe_base64_decode(uidb64))
		user = User.objects.get(pk=uid)
	except (TypeError, ValueError, OverflowError, User.DoesNotExist):
		user = None

	if user is not None and account_activation_token.check_token(user, token):
		return render(request, 'clientportal/reset_password.html', {'uidb64': uidb64})
	else:
		return HttpResponse('Fail to activate your account.')


def login(request):
	if request.method == 'POST':
	
		uemail = request.POST['email']
		upass = request.POST['password']

		try:
			user = authenticate(useremail=uemail, password=upass)
			if not user.is_active:
				messages.error(request, 'Your Profile is not active. Search Activation Link in your Inbox (Spam Folder)')
				return HttpResponseRedirect('/user/un_confirm/')
			
			else:
				userprofile = UserProfile.objects.get(userdata=user)
				
				if userprofile.is_confirm is True:
					auth_login(request, user)
					return redirect('/dashboard/')
			
				else:
					messages.error(request, 'Your Profile is not active. Search Activation Link in your Inbox (Spam Folder)')
					return HttpResponseRedirect('/user/un_confirm/')	

		except:
			messages.error(request, 'Please enter correct email & password')
			return redirect('/user/login/')	

	return render(request, 'clientportal/login.html')


@login_required(login_url="/user/login/")
def logout(request):
	django_logout(request)
	return HttpResponseRedirect('/user/login/')


@login_required(login_url="/user/login/")
def dashboard(request):
	''' User Dashboard '''
	return render(request, 'clientportal/dashboard.html')


def forget_password(request):
	if request.method == 'POST':
		useremail = request.POST['email']
		if User.objects.filter(email=useremail).exists():
			reset_password_token(request)
			messages.success(request, 'Please check your inbox (and your spam folder) <br>you should have received an email with a confirmation link for reset password')
			return HttpResponseRedirect('/user/un_confirm/')
		else:
			messages.error(request, 'Entered crediential not exist in database')
			return redirect('/user/forget_password/')
	return render(request, 'clientportal/forget_password.html')


def reset_password(request, uidb64):
	if request.method == 'POST':

		uid = force_text(urlsafe_base64_decode(uidb64))
		user = User.objects.get(id=uid)
		password = request.POST['password']
		user.set_password(password)
		user.save()
		messages.success(request, 'Your Password changed Successfully')
		return redirect('/user/login')

	return render(request, 'clientportal/reset_password.html')
