from django.test import TestCase, Client
from django.urls import reverse
from .models import Code

class CodeModelTests(TestCase):
    def test_return_not_null_200(self):
        """
        A GET to /api/id/<valid code> returns a non-null 200 response.
        """
        client = Client()
        response = client.get('/api/id/03111000-2')
        self.assertIs(response.status_code, 200)
        self.assertContains(response.body, 'id : 03111000-2, name : Graines')