from django.shortcuts import render,redirect
from.forms import CompanyForm,ProductForm
from.models import Company

# Create your views here.
def index(request):
    return render(request,"index.html")

def add_company(request):
    if request.method == 'GET':
        form=CompanyForm()
        return render(request,'add_company.html',context={'company_form':form})
    elif request.method == 'POST':
        form=CompanyForm(request.POST)
        if form.is_valid():
            form.save()
        else:
            return render(request, 'add_company.html',context={'company_form':form})
        return redirect('list_company')

def list_company(request):
    company_list=Company.objects.all()
    return render(request,'list_company.html',context={'company_list':company_list})

def edit_company(request):
    company=Company.objects.get(id=id)
    if request.method == 'GET':
        edit_company=CompanyForm(isinstance=company)
        return render(request,'edit_company.html',context={'edit_company':edit_company,'id':company.id})
    elif request.method == 'POST':
        edit_company=CompanyForm(request.POST,instance=company)
        if edit_company.is_valid():
            edit_company.save()
        else:
            return render(request, 'edit_company.html', context={'edit_company': edit_company, 'id': company.id})
        return redirect('list_company')



