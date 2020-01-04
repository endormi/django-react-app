from rest_framework import status
from rest_framework.test import APITestCase
from testfixtures.tests.sample1 import str_today_1


class LangTests(APITestCase):
    def test_languages_url(self):
        """
        Ensure we can get an object.
        """
        url = ('/languages/')
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)


    def test_languages_url_post(self):
        """
        Ensure we can create a new object.
        """
        data = {'name': 'C', 'paradigm': 'Imperative (procedural), structured', 'created_by': 'Dennis Ritchie'}
        url = ('/languages/')
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)


class FaangmTests(APITestCase):
    def test_faangm_url(self):
        """
        Ensure we can get an object.
        """
        url = ('/faangm/')
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_faangm_url_post(self):
        # Ensure we can create a new object.
        data = {'name': 'Pied Piper', 'founders': 'Richard Hendricks', 'created': str_today_1(), 'location': 'Erlich Bachman\'s business incubator'}
        url = ('/faangm/')
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
