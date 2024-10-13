from django.shortcuts import render, redirect, reverse
from django.http import HttpResponse, HttpRequest, Http404
from django.views.generic import DetailView, DeleteView, UpdateView
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from .models import Contracts
from .forms import NewContractForm


@login_required(login_url='staff:login')
@permission_required('crm.view_contracts', raise_exception=True)
def contracts_list(request: HttpRequest) -> HttpResponse:
    context = {
        "contracts": Contracts.objects.all()
    }
    return render(request, "contracts/contracts-list.html", context=context)


@login_required(login_url='staff:login')
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
            url = reverse('contracts:contracts')
            return redirect(url)
    else:
        form = NewContractForm()
    context = {
        "form": form,
    }
    return render(request, 'contracts/contracts-create.html', context=context)


class ContractDetail(LoginRequiredMixin, PermissionRequiredMixin, DetailView):
    template_name = 'contracts/contracts-detail.html'
    queryset = Contracts.objects.prefetch_related('service', 'user')
    context_object_name = 'object'
    permission_required = 'crm.view_contracts'

    def get(self, request, *args, **kwargs):
        try:
            return super().get(request, *args, **kwargs)
        except Http404:
            return redirect(reverse('contracts:contracts'))


class ContractDelete(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    template_name = 'contracts/contracts-delete.html'
    queryset = Contracts.objects.prefetch_related('service', 'user')
    context_object_name = 'object'
    success_url = reverse_lazy("contracts:contracts")
    permission_required = 'crm.delete_contracts'

    def get(self, request, *args, **kwargs):
        try:
            return super().get(request, *args, **kwargs)
        except Http404:
            return redirect(reverse('contracts:contracts'))


class ContractEdit(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    model = Contracts
    template_name = 'contracts/contracts-edit.html'
    fields = ['name', 'service', 'file', 'contract_date', 'period', 'total_cost', 'user']
    success_url = reverse_lazy("contracts:contracts")
    permission_required = 'crm.change_contracts'

    def get(self, request, *args, **kwargs):
        try:
            return super().get(request, *args, **kwargs)
        except Http404:
            return redirect(reverse('contracts:contracts'))