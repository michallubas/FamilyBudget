from rest_framework import viewsets
from .serializers import BudgetSerializer, InOutSerializer, UserSerializer
from .models import Budget, InOut
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated, AllowAny
from django.contrib.auth.models import User


class BudgetViewSet(viewsets.ModelViewSet):
    serializer_class = BudgetSerializer
    queryset = Budget.objects.all()
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated, )

class InoutViewSet(viewsets.ModelViewSet):
    serializer_class = InOutSerializer
    queryset = InOut.objects.all()
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)

class UserViewSet(viewsets.ModelViewSet):
    serializer_class = UserSerializer
    queryset = User.objects.all()
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)
