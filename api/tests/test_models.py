
from django.test import TestCase
from api.models import Budget, InOut
from datetime import datetime
from django.contrib.auth.models import User


class TestModels(TestCase):

    def setUp(self):
        self.budget1 =  Budget.objects.create(
            name = 'Budget 1',
            description = "Temp budget",
            data = datetime.now(),

        )
        self.user1 = User.objects.create_user(
            id=10,
            username='tempUser')

        InOut.objects.create(
            budget = self.budget1,
            category='food',
            user = self.user1,
            amount= 30,
            data=datetime.now()
        )

        InOut.objects.create(
            budget = self.budget1,
            category='food',
            user = self.user1,
            amount= 30,
            data=datetime.now()
        )


    def test_budget_balance(self):
        tempBalance = self.budget1.balance()

        self.assertEqual(tempBalance, 60)


