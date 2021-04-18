from django.contrib import admin
from django.urls import path
from django.conf.urls import include
from rest_framework.authtoken.views import obtain_auth_token
from api.views import home_view, budget_create_view, budget_list_view,budget_find_view, inout_list_view


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('api.urls')),
    path('auth/', obtain_auth_token),
    path('', home_view),

    path('budget_create', budget_create_view, name = 'budget_create'),
    path('budget_list/', budget_list_view, name ='budget_list' ),
    path('inout_list/', inout_list_view, name ='inout_list' ),
    path('budget_find/', budget_find_view, name = 'budget_find' ),

]
