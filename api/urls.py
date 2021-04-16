from django.contrib import admin
from django.urls import path
from django.conf.urls import include
from rest_framework import routers
from .views import BudgetViewSet, InoutViewSet, UserViewSet, LastInOutsViewSet, RangeInOutsViewSet

router = routers.DefaultRouter()
router.register('budgets', BudgetViewSet)
router.register('inouts' , InoutViewSet)
router.register('users', UserViewSet)
router.register(r'lastinouts/(?P<num>\d+)', LastInOutsViewSet)
router.register(r'rangeinouts/(?P<start>\d+)/(?P<finish>\d+)', RangeInOutsViewSet)

urlpatterns = [
    path('', include(router.urls)),

]
