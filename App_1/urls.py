from django.urls import path
from App_1.views import *

urlpatterns = [   
    path('', home, name = "inicio"), 
    path('employee/', employee, name = "empleados"),
    path('store/', store, name = "locales"),
    path('product/', product, name = "productos"),
]
