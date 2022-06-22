from django.urls import path
from app1 import views

urlpatterns = [
    path("list_company",views.list_company,name='list_company'),
    path("add_company",views.add_company,name='add_company')
]