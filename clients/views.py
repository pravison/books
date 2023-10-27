from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import TenantRegistrationForm
from . models import Client, Domain
from django_tenants.utils import schema_context
from django.contrib.auth.models import User
from homepage.models import Company, Contact_us, Social_Links

# Create your views here.

def tenantRegistration(request):
    infos = Company.objects.order_by('id')[:1]
    contacts_infos = Contact_us.objects.order_by('id')[:1]
    links = Social_Links.objects.all()
    if request.method == 'POST':
        form = TenantRegistrationForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            business_name = form.cleaned_data['business_name']
            phone = form.cleaned_data['phone']
            email = form.cleaned_data['email']
            location = form.cleaned_data['location']
            refferal_code = form.cleaned_data['refferal_code']
            # will write th elogic to handle ontrial and paid until
            on_trial = True
            paid_until = '2024-07-05'

            def remove(business_name):
                return "".join(business_name.split())
            business = remove(business_name)
            business_lower = business.lower()

            #create tenant
            new_tenant = Client(schema_name=business_lower, name=name, business_name=business_name, refferal_code=refferal_code, email=email, phone=phone, location=location, on_trial=on_trial, paid_until=paid_until)
            new_tenant.save()

            domain = Domain()
            domain.domain = business_lower + '.localhost'
            #domain.domain = business_lower + '.frontend.accountsmonitor.co.ke/'
            domain.tenant = new_tenant
            domain.is_primary= True
            domain.save()

            return redirect('http://localhost:3000/')
            #return redirect('https://frontend.accountsmonitor.co.ke/')
    else:
        form = TenantRegistrationForm()
    context = {
        'form':form,
        'infos': infos,
        'contacts_infos': contacts_infos,
        'links' :links

    }
    return render(request, 'register.html', context)