from django.test import TestCase, Client
from django.urls import reverse
from api.models import Code
# Create your tests here.

class AppTests(TestCase):

    @classmethod
    def setUpTestData(cls):
        cpvs = [
            {
                'id': '03111800-0',
                'name': 'Graines de fruits',
                'parent': ''
            },
            {
                'id': '03111000-2',
                'name': 'Graines',
                'parent': ''
            },
            {
                'id': '38435000-3',
                'name': 'Détecteurs de fluides',
                'parent': ''
            }
        ]

        for cpv in cpvs:
            cls.code = Code.objects.create(id=cpv['id'], name=cpv['name'])

    def test_return_html_200(self):
        """
        A GET to / returns a html 200 response.
        """
        client = Client()
        response = client.get(reverse('app:index'))
        assert('html' in response.headers['Content-Type'])
        self.assertEqual(response.status_code, 200)

    def test_cpv_fulltext(self):
        """
        A GET to /?text=<text> returns a list of CPVs that contain this text.
        """
        client = Client()
        response = client.get(reverse('app:index') + '?text="grain"')
        self.assertContains(response,'<li',count=2, status_code=200, html=False)
