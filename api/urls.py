from django.contrib import admin
from django.urls import path
from django.conf.urls import include
from rest_framework import routers
from .views import BudgetViewSet, InoutViewSet

router = routers.DefaultRouter()
router.register('budgets', BudgetViewSet)
router.register('inouts' , InoutViewSet)

urlpatterns = [
    path('', include(router.urls)),

]
