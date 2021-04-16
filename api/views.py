from rest_framework import viewsets
from .serializers import BudgetSerializer, InOutSerializer
from .models import Budget, InOut


class BudgetViewSet(viewsets.ModelViewSet):
    serializer_class = BudgetSerializer
    queryset = Budget.objects.all()

class InoutViewSet(viewsets.ModelViewSet):
    serializer_class = InOutSerializer
    queryset = InOut.objects.all()