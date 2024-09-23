from django.shortcuts import render, redirect, reverse
from django.http import HttpResponse, HttpRequest
from django.views.generic import DetailView, DeleteView, UpdateView
from django.urls import reverse_lazy
from django.contrib.auth import logout

from .models import Services, Advertisements, Customer, Contracts
from .forms import NewServiceForm, NewAdvertisementForm, NewCustomerForm, NewContractForm, NewActiveCustomerForm


# Create your views here.
def services_list(request: HttpRequest) -> HttpResponse:
    context = {
        "products": Services.objects.all()
    }
    return render(request, "crm/products/products-list.html", context=context)


def advertisements_list(request: HttpRequest) -> HttpResponse:
    context = {
        "ads": Advertisements.objects.all()
    }
    return render(request, "crm/ads/ads-list.html", context=context)


def customers_list(request: HttpRequest) -> HttpResponse:
    context = {
        "leads": Customer.objects.filter(status=False).all()
    }
    return render(request, "crm/leads/leads-list.html", context=context)


def customers_active_list(request: HttpRequest) -> HttpResponse:
    context = {
        "customers": Customer.objects.filter(status=True).all()
    }
    return render(request, "crm/customers/customers-list.html", context=context)


def contacts_list(request: HttpRequest) -> HttpResponse:
    context = {
        "contracts": Contracts.objects.all()
    }
    return render(request, "crm/contracts/contracts-list.html", context=context)


def new_service(request: HttpRequest) -> HttpResponse:
    if request.method == "POST":
        form = NewServiceForm(request.POST)
        if form.is_valid():
            Services.objects.create(**form.cleaned_data)
            url = reverse('crm:services')
            return redirect(url)
    else:
        form = NewServiceForm()
    context = {
        "form": form,
    }
    return render(request, 'crm/products/products-create.html', context=context)


def new_advertisement(request: HttpRequest) -> HttpResponse:
    if request.method == "POST":
        form = NewAdvertisementForm(request.POST)
        if form.is_valid():
            Advertisements.objects.create(**form.cleaned_data)
            url = reverse('crm:advertisements')
            return redirect(url)
    else:
        form = NewAdvertisementForm()
    context = {
        "form": form,
    }
    return render(request, 'crm/ads/ads-create.html', context=context)


def new_customer(request: HttpRequest) -> HttpResponse:
    if request.method == "POST":
        form = NewCustomerForm(request.POST)
        if form.is_valid():
            Customer.objects.create(**form.cleaned_data)
            url = reverse('crm:leads')
            return redirect(url)
    else:
        form = NewCustomerForm()
    context = {
        "form": form,
    }
    return render(request, 'crm/leads/leads-create.html', context=context)


def new_active_customer(request: HttpRequest) -> HttpResponse:
    if request.method == "POST":
        form = NewActiveCustomerForm(request.POST)
        if form.is_valid():
            customer = form.cleaned_data['user']
            advertisement = form.cleaned_data['advertisement']

            customer.status = True
            customer.advertisement = advertisement
            customer.save()
            url = reverse('crm:customers')
            return redirect(url)
    else:
        form = NewActiveCustomerForm()
    context = {
        "form": form,
    }
    return render(request, 'crm/customers/customers-create.html', context=context)


def new_contract(request: HttpRequest) -> HttpResponse:
    if request.method == "POST":
        form = NewContractForm(request.POST, request.FILES)
        if form.is_valid():
            contract = Contracts(
                name=form.cleaned_data['name'],
                service=form.cleaned_data['service'],
                file=form.cleaned_data['file'],
                contract_date=form.cleaned_data['contract_date'],
                period=form.cleaned_data['period'],
                total_cost=form.cleaned_data['total_cost'],
                user=form.cleaned_data['user'],
            )
            contract.save()
            url = reverse('crm:contracts')
            return redirect(url)
    else:
        form = NewContractForm()
    context = {
        "form": form,
    }
    return render(request, 'crm/contracts/contracts-create.html', context=context)


class ServiceDetail(DetailView):
    template_name = 'crm/products/products-detail.html'
    queryset = Services.objects.prefetch_related()
    context_object_name = 'object'


class AdvertisementDetail(DetailView):
    template_name = 'crm/ads/ads-detail.html'
    queryset = Advertisements.objects.prefetch_related('service')
    context_object_name = 'object'


class LeadDetail(DetailView):
    template_name = 'crm/leads/leads-detail.html'
    queryset = Customer.objects.prefetch_related('advertisement')
    context_object_name = 'object'


class CustomerDetail(DetailView):
    template_name = 'crm/customers/customers-detail.html'
    queryset = Customer.objects.prefetch_related('advertisement')
    context_object_name = 'object'


class ContractDetail(DetailView):
    template_name = 'crm/contracts/contracts-detail.html'
    queryset = Contracts.objects.prefetch_related('service', 'user')
    context_object_name = 'object'


class ServiceDetele(DeleteView):
    template_name = 'crm/products/products-delete.html'
    queryset = Services.objects.prefetch_related()
    context_object_name = 'object'
    success_url = reverse_lazy("crm:services")


class AdvertisementDelete(DeleteView):
    template_name = 'crm/ads/ads-delete.html'
    queryset = Advertisements.objects.prefetch_related('service')
    context_object_name = 'object'
    success_url = reverse_lazy("crm:advertisements")


class LeadDelete(DeleteView):
    template_name = 'crm/leads/leads-delete.html'
    queryset = Customer.objects.prefetch_related('advertisement')
    context_object_name = 'object'
    success_url = reverse_lazy("crm:leads")


class CustomerDelete(DeleteView):
    template_name = 'crm/customers/customers-delete.html'
    queryset = Customer.objects.prefetch_related('advertisement')
    context_object_name = 'object'
    success_url = reverse_lazy("crm:customers")


class ContractDelete(DeleteView):
    template_name = 'crm/contracts/contracts-delete.html'
    queryset = Contracts.objects.prefetch_related('service', 'user')
    context_object_name = 'object'
    success_url = reverse_lazy("crm:contracts")


class ServiceEdit(UpdateView):
    model = Services
    template_name = 'crm/products/products-edit.html'
    fields = ['name', 'description', 'cost']
    success_url = reverse_lazy("crm:services")


class AdvertisementEdit(UpdateView):
    model = Advertisements
    template_name = 'crm/ads/ads-edit.html'
    fields = ['name', 'channel', 'budget', 'service']
    success_url = reverse_lazy("crm:advertisements")


class LeadEdit(UpdateView):
    model = Customer
    template_name = 'crm/leads/leads-edit.html'
    fields = ['last_name', 'first_name', 'surname', 'phone', 'email']
    success_url = reverse_lazy("crm:leads")


class CustomerEdit(UpdateView):
    model = Customer
    template_name = 'crm/customers/customers-edit.html'
    fields = ['advertisement', 'status']
    success_url = reverse_lazy("crm:customers")


class ContractEdit(UpdateView):
    model = Contracts
    template_name = 'crm/contracts/contracts-edit.html'
    fields = ['name', 'service', 'file', 'contract_date', 'period', 'total_cost', 'user']
    success_url = reverse_lazy("crm:contracts")


def logout_view(request: HttpRequest):
    logout(request)
    return redirect("crm:login")