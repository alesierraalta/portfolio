from django.test import TestCase
from django.urls import reverse

class IndexPageTest(TestCase):
    def test_index_page_loads(self):
        response = self.client.get(reverse('index'))
        self.assertEqual(response.status_code, 200)

    def test_inicioml_page_status_code(self):
        response = self.client.get(reverse('inicioml'))
        self.assertEqual(response.status_code, 200)
