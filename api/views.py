from rest_framework import viewsets
from .serializers import BudgetSerializer, InOutSerializer, UserSerializer
from .models import Budget, InOut
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated, AllowAny
from django.contrib.auth.models import User
from datetime import datetime
from django.shortcuts import render
from .forms import BudgetForm, RawBudgetForm, RawBudgetListForm

class BudgetViewSet(viewsets.ModelViewSet):
    serializer_class = BudgetSerializer
    queryset = Budget.objects.all()
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)


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


def budget_create_view(request):
    form = RawBudgetForm()
    if request.method == "POST":
        form = RawBudgetForm(request.POST or None)
        if form.is_valid():
            print('tuu')
            print(form.cleaned_data)
            Budget.objects.create(**form.cleaned_data)
            form = RawBudgetForm()
        else:
            print(form.errors)
    context = {
        "form": form
    }
    return render(request, "budgets/budget_create.html", context)

def budget_list_view(request):
    queryset = Budget.objects.all()
    context = {
        "object_list": queryset
    }

    return render(request, "budgets/budget_list.html", context)

def inout_list_view(request):
    queryset = InOut.objects.all()
    context = {
        "object_list": queryset
    }

    return render(request, "inouts/inout_list.html", context)

def budget_find_view(request):
    form = RawBudgetListForm()

    if request.method == "POST":
        form = RawBudgetListForm(request.POST)
        if form.is_valid():
            tempId=request.POST['id']

            obj = Budget.objects.get(id=tempId)
            context = {
                'object': obj
            }
            return render(request, "budgets/budget_detail.html", context)

        else:
            print(form.errors)

    context = {
        'form': form
    }

    return render(request, "budgets/budget_find.html", context)


def budget_detail_view(request):
    obj = Budget.objects.get(id=1)
    context = {
        'object': obj
    }

    return render(request, "budgets/budget_detail.html", context)


def budget_create_temp_view(request):
    print("GET: " ,request.GET)
    print("POST: ",request.POST)
    if request.method == "POST":
        print("POST budget: ", request.POST['budget'])
        title = request.POST.get('budget')
        print(title)
    context = {
    }
    return render(request, "budgets/budget_create_temp.html", context)


def home_view(request, *args, **kwargs):
    print(args, kwargs)
    print(request.user)
    context1 = {
        'form': 'temp',
        'html_test': '<h1> temp</p1>'
    }
    return render(request, "home.html", context1)





def budget_create_view_expired(request):
    form = BudgetForm(request.POST or None)
    if form.is_valid():
        form.save()
        form = BudgetForm()

    context = {
        'form': form
    }
    return render(request, "budgets/budget_create.html", context)


# I will no use pure html
# def budget_create_temp_view(request):
#     print("GET: " ,request.GET)
#     print("POST: ",request.POST)
#     if request.method == "POST":
#         print("POST budget: ", request.POST['budget'])
#         title = request.POST.get('budget')
#         print(title)
#     context = {
#     }
#     return render(request, "budgets/budget_create_temp.html", context)