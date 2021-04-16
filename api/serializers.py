from rest_framework import serializers
from .models import Budget, InOut


class BudgetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Budget
        fields = ['name', 'description', 'balance']


class InOutSerializer(serializers.ModelSerializer):
    class Meta:
        model = InOut
        fields = ['budget', 'user', 'category', 'amount']
