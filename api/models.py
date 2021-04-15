from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator, RegexValidator


class Budget(models.Model):
    name = models.CharField(max_length=32)
    description = models.CharField(max_length=32)

    def __str__(self):
        return f"Budget {self.name}, its {self.description} "


tempCategory = RegexValidator('home|shopping|food|vehicles|vacation|school|communication',
                              'Only: home, shopping, food, vehicles, vacation, school, communication categories allowed')


class InOut(models.Model):
    budget = models.ForeignKey(Budget, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.CharField(max_length=16, validators=[tempCategory])
    amount = models.DecimalField(decimal_places=2, max_digits=8,
                                 validators=[MinValueValidator(100), MaxValueValidator(100)])

    def __str__(self):
        return f"Income/expenses for category {self.category} "
