from django.test import TestCase
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse



class ModelTestCase(TestCase):
    """This class defines the test suite for the bucketlist model."""

    def setUp(self):
        """Define the test client and other test variables."""
        self.user = User.objects.create(email="harsh@gmail.com", username="harsh")
        self.user.set_password("password")
        self.user.save()

    def test_user_is_active(self):
        self.assertTrue(self.user.is_active)

    def test_check_username_is_correct(self):
        username = self.user.username
        userdata = User.objects.get(pk=self.user.pk)
        import pdb; pdb.set_trace()
        self.assertEqual(userdata.username, username)     

    # def test_user_is_active(self):
    #     self.assertTrue(self.user.is_active)

    # def test_model_returns_readable_representation(self):
    #     """Test a readable string is returned for the model instance."""
    #     self.assertEqual(str(self.bucketlist), self.name)
