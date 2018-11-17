from django.contrib.auth.models import User
from django.urls import reverse
from django.test.client import Client
import unittest

class LoginTestCase(unittest.TestCase):

    def testLogin_success(self):
        self.client = Client()
        self.user = User.objects.create_user('pranav', 'pranav@vitamin.io', 'hello')
        self.client.login(username='pranav', password='hello')
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)

    def testLogin_error(self):
        self.client = Client()
        self.user = User.objects.create_user('mahesh', 'mahesh@vitamin.io', 'hello')
        self.client.login(username='mahesh', password='_hello')
        response = self.client.get(reverse('home'))
        self.assertNotEqual(response.status_code, 200)
