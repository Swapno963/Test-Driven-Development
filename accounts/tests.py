from django.test import TestCase
from django.urls import reverse
from http import HTTPStatus
# Create your tests here.


class AccountCreationTest(TestCase):

    def test_signup_page_exists(self):
        responce = self.client.get(reverse('signup_page'))

        self.assertEqual(responce.status_code, HTTPStatus.OK)        
        self.assertTemplateUsed('accounts/register.html')
        self.assertContains(responce, "Create Your Account Today")