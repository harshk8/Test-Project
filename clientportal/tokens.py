from django.contrib.auth.tokens import PasswordResetTokenGenerator
from django.utils import six

from django.utils import timezone
import datetime


class AccountActivationTokenGenerator(PasswordResetTokenGenerator):

    def _make_hash_value(self, user, timestamp):
      	return (
            six.text_type(user.pk) + six.text_type(timestamp) 
        )

account_activation_token = AccountActivationTokenGenerator()