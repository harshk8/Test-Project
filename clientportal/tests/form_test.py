from django.test import TestCase
from django.contrib.auth.models import User
from clientportal import forms 


class Form_Test(TestCase):
    """This class defines the test suite for the bucketlist model."""

    def test_form_valid(self):
    	form = forms.UserForm(data={'email': 'harsh@gmail.com', 'password': 'password'})
    	self.assertTrue(form.is_valid())
