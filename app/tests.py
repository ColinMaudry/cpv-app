from django.test import TestCase, Client
from django.urls import reverse
# Create your tests here.

class AppTests(TestCase):
    def test_return_html_200(self):
        """
        A GET to / returns a html 200 response.
        """
        client = Client()
        response = client.get(reverse('app:index'))
        assert('html' in response.headers['Content-Type'])
        self.assertIs(response.status_code, 200)
