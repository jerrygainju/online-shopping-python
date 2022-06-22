from django import forms
from app1.models import Company,Product

class CompanyForm(forms.Form):
    class Meta:
        model=Company
        fields="__all__"

class ProductForm(forms.Form):
    class Meta:
        model=Product
        fields="__all__"