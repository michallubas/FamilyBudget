from django.contrib import admin
from django.urls import path
from django.conf.urls import include
from rest_framework import routers
from .views import BudgetViewSet, InoutViewSet, UserViewSet, LastInOutsViewSet, RangeInOutsViewSet, budget_detail_view, budget_create_view, budget_create_temp_view, budget_list_view

router = routers.DefaultRouter()
router.register('budgets', BudgetViewSet)
router.register('inouts' , InoutViewSet)
router.register('users', UserViewSet)
router.register(r'lastinouts/(?P<num>\d+)', LastInOutsViewSet)
router.register(r'rangeinouts/(?P<start>\d+)/(?P<finish>\d+)', RangeInOutsViewSet)


urlpatterns = [
    path('', include(router.urls)),


    path('budget_create_temp/', budget_create_temp_view, name = 'budget_create')

]

# path('budget_detail', budget_detail_view),