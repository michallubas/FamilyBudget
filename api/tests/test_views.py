
from django.test import TestCase, Client
from django.urls import reverse

class TestViews(TestCase):

    def setUp(self):
        self.client = Client()
        self.budget_list_url = reverse('budget_list')
        self.inout_list_url = reverse('inout_list')

    def test_budget_list_GET(self):
        response = self.client.get(self.budget_list_url)

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'budgets/budget_list.html')

    def test_inout_list_GET(self):
        response = self.client.get(self.inout_list_url)

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'inouts/inout_list.html')


