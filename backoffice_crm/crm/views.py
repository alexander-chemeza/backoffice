from django.shortcuts import render
from django.http import HttpResponse, HttpRequest

from .forms import NewServiceForm, NewAdvertisementForm, NewCustomerForm, NewContractForm


# Create your views here.
def new_service(request: HttpRequest) -> HttpResponse:
    context = {
        "form": NewServiceForm(),
    }
    return render(request, 'crm/products/products-create.html', context=context)


def new_advertisement(request: HttpRequest) -> HttpResponse:
    context = {
        "form": NewAdvertisementForm(),
    }
    return render(request, 'crm/ads/ads-create.html', context=context)


def new_customer(request: HttpRequest) -> HttpResponse:
    context = {
        "form": NewCustomerForm(),
    }
    return render(request, 'crm/customers/customers-create.html', context=context)


def new_contract(request: HttpRequest) -> HttpResponse:
    context = {
        "form": NewContractForm(),
    }
    return render(request, 'crm/contracts/contracts-create.html', context=context)