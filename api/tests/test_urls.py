from django.test import SimpleTestCase
from django.urls import reverse, resolve
from ..views import inout_list_view, budget_find_view, budget_list_view, BudgetViewSet

class TestUrls(SimpleTestCase):

    def test_budget_list_url_is_resolved(self):

        url = reverse('budget_list')
        # print(resolve(url))
        self.assertEqual(resolve(url).func, budget_list_view)

    def test_inout_list_url_is_resolved(self):

        url = reverse('inout_list')
        self.assertEqual(resolve(url).func, inout_list_view)

    def test_budget_find_url_is_resolved(self):

        url = reverse('budget_find')
        self.assertEqual(resolve(url).func, budget_find_view)

    def test_budget_find_url_is_resolved(self):

        url = reverse('budget_find')
        self.assertEqual(resolve(url).func, budget_find_view)

