from django.test import TestCase
from django.urls import reverse


class TestItsAlive(TestCase):
    def test_its_alive(self):
        url = reverse('employee:its_alive')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), {'message': 'its_alive'})
