from django.test import TestCase, Client
from django.urls import reverse
from .models import Code

class CodeModelTests(TestCase):

    @classmethod
    def setUpTestData(cls):
        cls.code = Code.objects.create(id='03111000-2', name='Graines')

    def test_return_not_null_200(self):
        """
        A GET to /api/id/<valid code> returns a non-null 200 response.
        """
        client = Client()
        response = client.get(reverse('api:code', kwargs = {'cpv_id': '03111000-2'}))
        self.assertIs(response.status_code, 200)
        self.assertContains(response, 'id : 03111000-2, name : Graines')