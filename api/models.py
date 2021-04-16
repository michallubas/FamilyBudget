from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator, RegexValidator
from rest_framework.decorators import action
from datetime import datetime

class Budget(models.Model):
    name = models.CharField(max_length=32)
    description = models.CharField(max_length=32)
    data = models.DateTimeField(default=datetime.now())

    def balance(self):
        getInOuts = InOut.objects.filter(budget=self)
        sum = 0
        for inout in getInOuts:
            sum+=inout.amount
        return sum

    def __str__(self):
        return f"Budget {self.name}, its {self.description} "



tempCategory = RegexValidator('home|shopping|food|vehicles|vacation|school|communication',
                              'Only: home, shopping, food, vehicles, vacation, school, communication categories allowed')


class InOut(models.Model):
    budget = models.ForeignKey(Budget, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.CharField(max_length=16, validators=[tempCategory])
    amount = models.DecimalField(decimal_places=2, max_digits=8,
                                 validators=[MinValueValidator(-1000), MaxValueValidator(1000)])
    data = models.DateTimeField(default=datetime.now())

    def __str__(self):
        return f"Income/expenses for category {self.category} "
