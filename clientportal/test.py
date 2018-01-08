from django.test import TestCase
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from . import views

from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode



class UserTestCase(TestCase):

    def setUp(self):
    	self.user = User.objects.create(email="harsh@gmail.com", username="harsh")
    	self.user.set_password("password")
    	self.user.save()
   	
    def test_signup(self):
    	url = '/user/signup/'
    	data = {"email": "dexter@gmail.com", 
    					"password": "123"}
    	response = self.client.post(url, data, follow=True)
    	# self.assertEqual(self.user.is_authenticated(), True)
    	self.assertEqual(response.status_code, 200)
    	userdata = response.context['user']
    	self.assertTrue(userdata.is_authenticated())

    def test_signup_already_existing_user(self):
    	url = '/user/signup/'
    	data = {"email": "harsh@gmail.com", 
    					"password": "123"}
    	response = self.client.post(url, data, follow=True)
    	# import pdb; pdb.set_trace()
    	self.assertEqual(response.status_code, 200)
    	userdata = response.context['user']
    	self.assertFalse(userdata.is_authenticated())

    # def test_activate_user(self):
    # 	response = self.client.force_authenticate(user=self.user)
    # 	# response = self.client.post(url, data, follow=True)
    # 	userdata = response.context['user']
    	
    # 	# self.assertEqual(response.status_code, 200)
    # 	# self.assertTrue(userdata.is_authenticated())
    # 	# import pdb; pdb.set_trace()
    # 	uid = urlsafe_base64_encode(force_bytes(userdata.pk))
    # 	token = views.account_activation_token.make_token(userdata)
    # 	import pdb; pdb.set_trace()
    # 	link = '/user/reset_activate/' + str(uid) + '/' + str(token) +'/'
    # 	response1 = self.client.get(link, follow=True)
    # 	self.assertEqual(response1.status_code, 200)


    def test_userlogin_with_correct_credientials(self):
    	url = '/user/login/'
    	data = {"email": self.user.email, 
    					"password": 'password'}
    	response = self.client.post(url, data, follow=True)
    
    	# self.assertEqual(self.user.is_authenticated(), True)
    	self.assertEqual(response.status_code, 200)
    	userdata = response.context['user']
    	self.assertTrue(userdata.is_authenticated())

    def test_userlogin_with_uncorrect_credientials(self):
    	url = '/user/login/'
    	data = {"email": self.user.email,
    					"password": 'UNKNOWNpassword'}
    	response = self.client.post(url, data, follow=True)
    	# import pdb; pdb.set_trace()
    	self.assertEqual(response.status_code, 200)
    	userdata = response.context['user']
    	self.assertFalse(userdata.is_authenticated())




