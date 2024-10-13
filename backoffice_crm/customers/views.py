from django.shortcuts import render, redirect, reverse
from django.http import HttpResponse, HttpRequest, Http404
from django.views.generic import DetailView, DeleteView, UpdateView
from django.urls import reverse_lazy
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin


from .models import Customers
from .forms import NewCustomerForm


@login_required(login_url='staff:login')
@permission_required('customers.view_customers', raise_exception=True)
def customers_active_list(request: HttpRequest) -> HttpResponse:
    context = {
        "customers": Customers.objects.all()
    }
    return render(request, "customers/customers-list.html", context=context)


@login_required(login_url='staff:login')
@permission_required('customers.add_customers', raise_exception=True)
@permission_required('customers.change_customers', raise_exception=True)
def new_active_customer(request: HttpRequest) -> HttpResponse:
    if request.method == "POST":
        form = NewCustomerForm(request.POST)
        if form.is_valid():
            lead = form.cleaned_data['user']
            advertisement = form.cleaned_data['advertisement']
            Customers.objects.create(lead=lead, advertisement=advertisement)
            url = reverse('customers:customers')
            return redirect(url)
    else:
        form = NewCustomerForm()
    context = {
        "form": form,
    }
    return render(request, 'customers/customers-create.html', context=context)


class CustomerDetail(LoginRequiredMixin, PermissionRequiredMixin, DetailView):
    template_name = 'customers/customers-detail.html'
    queryset = Customers.objects.prefetch_related('advertisement')
    context_object_name = 'object'
    permission_required = 'customers.view_customers'

    def get(self, request, *args, **kwargs):
        try:
            return super().get(request, *args, **kwargs)
        except Http404:
            return redirect(reverse('customers:customers'))


class CustomerDelete(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    template_name = 'customers/customers-delete.html'
    queryset = Customers.objects.prefetch_related('advertisement')
    context_object_name = 'object'
    success_url = reverse_lazy("customers:customers")
    permission_required = 'customers.delete_customers'

    def get(self, request, *args, **kwargs):
        try:
            return super().get(request, *args, **kwargs)
        except Http404:
            return redirect(reverse('customers:customers'))


class CustomerEdit(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    model = Customers
    template_name = 'customers/customers-edit.html'
    fields = ['lead', 'advertisement']
    success_url = reverse_lazy("customers:customers")
    permission_required = 'customers.change_customers'

    def get(self, request, *args, **kwargs):
        try:
            return super().get(request, *args, **kwargs)
        except Http404:
            return redirect(reverse('customers:customers'))