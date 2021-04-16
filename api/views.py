from rest_framework import viewsets
from .serializers import BudgetSerializer, InOutSerializer, UserSerializer
from .models import Budget, InOut
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated, AllowAny
from django.contrib.auth.models import User
from datetime import datetime


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


class LastInOutsViewSet(viewsets.ModelViewSet):
    serializer_class = InOutSerializer
    queryset = InOut.objects.all()
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        temp_num = int(self.kwargs['num'])
        return InOut.objects.order_by('-id')[:temp_num]


class RangeInOutsViewSet(viewsets.ModelViewSet):
    serializer_class = InOutSerializer
    queryset = InOut.objects.all()
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        temp_start = int(self.kwargs['start'])
        temp_finish = int(self.kwargs['finish'])
        dt_object_start = datetime.fromtimestamp(temp_start)
        dt_object_finish = datetime.fromtimestamp(temp_finish)
        return InOut.objects.filter(data__range=[dt_object_start, dt_object_finish])

