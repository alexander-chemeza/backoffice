from django.shortcuts import render, redirect, reverse
from django.http import HttpResponse, HttpRequest, Http404
from django.views.generic import DetailView, DeleteView, UpdateView
from django.urls import reverse_lazy
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin


from .models import Services, Advertisements, Customer, Contracts
from .forms import NewServiceForm, NewAdvertisementForm, NewCustomerForm, NewContractForm, NewActiveCustomerForm

@login_required(login_url='crm:login')
@permission_required('crm.view_services', raise_exception=True)
def services_list(request: HttpRequest) -> HttpResponse:
    context = {
        "products": Services.objects.all()
    }
    return render(request, "crm/products/products-list.html", context=context)


@login_required(login_url='crm:login')
@permission_required('crm.view_advertisements', raise_exception=True)
def advertisements_list(request: HttpRequest) -> HttpResponse:
    context = {
        "ads": Advertisements.objects.all()
    }
    return render(request, "crm/ads/ads-list.html", context=context)


@login_required(login_url='crm:login')
@permission_required('crm.view_customer', raise_exception=True)
def customers_list(request: HttpRequest) -> HttpResponse:
    context = {
        "leads": Customer.objects.filter(status=False).all()
    }
    return render(request, "crm/leads/leads-list.html", context=context)


@login_required(login_url='crm:login')
@permission_required('crm.view_customer', raise_exception=True)
def customers_active_list(request: HttpRequest) -> HttpResponse:
    context = {
        "customers": Customer.objects.filter(status=True).all()
    }
    return render(request, "crm/customers/customers-list.html", context=context)


@login_required(login_url='crm:login')
@permission_required('crm.view_contracts', raise_exception=True)
def contracts_list(request: HttpRequest) -> HttpResponse:
    context = {
        "contracts": Contracts.objects.all()
    }
    return render(request, "crm/contracts/contracts-list.html", context=context)


@login_required(login_url='crm:login')
@permission_required('crm.add_services', raise_exception=True)
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


@login_required(login_url='crm:login')
@permission_required('crm.add_advertisements', raise_exception=True)
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


@login_required(login_url='crm:login')
@permission_required('crm.add_customer', raise_exception=True)
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


@login_required(login_url='crm:login')
@permission_required('crm.add_customer', raise_exception=True)
@permission_required('crm.change_customer', raise_exception=True)
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


@login_required(login_url='crm:login')
@permission_required('crm.add_contracts', raise_exception=True)
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


class ServiceDetail(LoginRequiredMixin, PermissionRequiredMixin, DetailView):
    template_name = 'crm/products/products-detail.html'
    queryset = Services.objects.prefetch_related()
    context_object_name = 'object'
    permission_required = 'crm.view_services'

    def get(self, request, *args, **kwargs):
        try:
            return super().get(request, *args, **kwargs)
        except Http404:
            return redirect(reverse('crm:services'))


class AdvertisementDetail(LoginRequiredMixin, PermissionRequiredMixin, DetailView):
    template_name = 'crm/ads/ads-detail.html'
    queryset = Advertisements.objects.prefetch_related('service')
    context_object_name = 'object'
    permission_required = 'crm.view_advertisements'

    def get(self, request, *args, **kwargs):
        try:
            return super().get(request, *args, **kwargs)
        except Http404:
            return redirect(reverse('crm:advertisements'))


class LeadDetail(LoginRequiredMixin, PermissionRequiredMixin, DetailView):
    template_name = 'crm/leads/leads-detail.html'
    queryset = Customer.objects.prefetch_related('advertisement')
    context_object_name = 'object'
    permission_required = 'crm.view_customer'

    def get(self, request, *args, **kwargs):
        try:
            return super().get(request, *args, **kwargs)
        except Http404:
            return redirect(reverse('crm:leads'))


class CustomerDetail(LoginRequiredMixin, PermissionRequiredMixin, DetailView):
    template_name = 'crm/customers/customers-detail.html'
    queryset = Customer.objects.prefetch_related('advertisement')
    context_object_name = 'object'
    permission_required = 'crm.view_customer'

    def get(self, request, *args, **kwargs):
        try:
            return super().get(request, *args, **kwargs)
        except Http404:
            return redirect(reverse('crm:customers'))


class ContractDetail(LoginRequiredMixin, PermissionRequiredMixin, DetailView):
    template_name = 'crm/contracts/contracts-detail.html'
    queryset = Contracts.objects.prefetch_related('service', 'user')
    context_object_name = 'object'
    permission_required = 'crm.view_contracts'

    def get(self, request, *args, **kwargs):
        try:
            return super().get(request, *args, **kwargs)
        except Http404:
            return redirect(reverse('crm:contracts'))


class ServiceDetele(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    template_name = 'crm/products/products-delete.html'
    queryset = Services.objects.prefetch_related()
    context_object_name = 'object'
    success_url = reverse_lazy("crm:services")
    permission_required = 'crm.delete_services'

    def get(self, request, *args, **kwargs):
        try:
            return super().get(request, *args, **kwargs)
        except Http404:
            return redirect(reverse('crm:services'))


class AdvertisementDelete(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    template_name = 'crm/ads/ads-delete.html'
    queryset = Advertisements.objects.prefetch_related('service')
    context_object_name = 'object'
    success_url = reverse_lazy("crm:advertisements")
    permission_required = 'crm.delete_advertisements'

    def get(self, request, *args, **kwargs):
        try:
            return super().get(request, *args, **kwargs)
        except Http404:
            return redirect(reverse('crm:advertisements'))


class LeadDelete(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    template_name = 'crm/leads/leads-delete.html'
    queryset = Customer.objects.prefetch_related('advertisement')
    context_object_name = 'object'
    success_url = reverse_lazy("crm:leads")
    permission_required = 'crm.delete_customer'

    def get(self, request, *args, **kwargs):
        try:
            return super().get(request, *args, **kwargs)
        except Http404:
            return redirect(reverse('crm:leads'))


class CustomerDelete(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    template_name = 'crm/customers/customers-delete.html'
    queryset = Customer.objects.prefetch_related('advertisement')
    context_object_name = 'object'
    success_url = reverse_lazy("crm:customers")
    permission_required = 'crm.delete_customer'

    def get(self, request, *args, **kwargs):
        try:
            return super().get(request, *args, **kwargs)
        except Http404:
            return redirect(reverse('crm:customers'))


class ContractDelete(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    template_name = 'crm/contracts/contracts-delete.html'
    queryset = Contracts.objects.prefetch_related('service', 'user')
    context_object_name = 'object'
    success_url = reverse_lazy("crm:contracts")
    permission_required = 'crm.delete_contracts'

    def get(self, request, *args, **kwargs):
        try:
            return super().get(request, *args, **kwargs)
        except Http404:
            return redirect(reverse('crm:contracts'))


class ServiceEdit(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    model = Services
    template_name = 'crm/products/products-edit.html'
    fields = ['name', 'description', 'cost']
    success_url = reverse_lazy("crm:services")
    permission_required = 'crm.change_services'

    def get(self, request, *args, **kwargs):
        try:
            return super().get(request, *args, **kwargs)
        except Http404:
            return redirect(reverse('crm:services'))


class AdvertisementEdit(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    model = Advertisements
    template_name = 'crm/ads/ads-edit.html'
    fields = ['name', 'channel', 'budget', 'service']
    success_url = reverse_lazy("crm:advertisements")
    permission_required = 'crm.change_advertisements'

    def get(self, request, *args, **kwargs):
        try:
            return super().get(request, *args, **kwargs)
        except Http404:
            return redirect(reverse('crm:advertisements'))


class LeadEdit(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    model = Customer
    template_name = 'crm/leads/leads-edit.html'
    fields = ['last_name', 'first_name', 'surname', 'phone', 'email']
    success_url = reverse_lazy("crm:leads")
    permission_required = 'crm.change_customer'

    def get(self, request, *args, **kwargs):
        try:
            return super().get(request, *args, **kwargs)
        except Http404:
            return redirect(reverse('crm:leads'))


class CustomerEdit(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    model = Customer
    template_name = 'crm/customers/customers-edit.html'
    fields = ['advertisement', 'status']
    success_url = reverse_lazy("crm:customers")
    permission_required = 'crm.change_customer'

    def get(self, request, *args, **kwargs):
        try:
            return super().get(request, *args, **kwargs)
        except Http404:
            return redirect(reverse('crm:customers'))


class ContractEdit(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    model = Contracts
    template_name = 'crm/contracts/contracts-edit.html'
    fields = ['name', 'service', 'file', 'contract_date', 'period', 'total_cost', 'user']
    success_url = reverse_lazy("crm:contracts")
    permission_required = 'crm.change_contracts'

    def get(self, request, *args, **kwargs):
        try:
            return super().get(request, *args, **kwargs)
        except Http404:
            return redirect(reverse('crm:contracts'))


def logout_view(request: HttpRequest):
    logout(request)
    return redirect("crm:login")


@login_required(login_url="crm:login")
def home_view(request: HttpRequest) -> HttpResponse:
    context = {
        "products_count": Services.objects.all().count(),
        "advertisements_count": Advertisements.objects.all().count(),
        "leads_count": Customer.objects.filter(status=False).all().count(),
        "customers_count": Customer.objects.filter(status=True).all().count(),
    }
    return render(request, "crm/users/index.html", context=context)