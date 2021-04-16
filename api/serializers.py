from rest_framework import serializers
from .models import Budget, InOut
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token

class BudgetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Budget
        fields = ['name', 'description', 'balance', 'data']


class InOutSerializer(serializers.ModelSerializer):
    class Meta:
        model = InOut
        fields = ['budget', 'user', 'category', 'amount', 'data']


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'password']
        extra_kwargs = {'password': {'write_only':True, 'required':True}}

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        Token.objects.create(user=user)
        return user
