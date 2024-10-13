from django.shortcuts import render, redirect, reverse
from django.http import HttpResponse, HttpRequest, Http404
from django.views.generic import DetailView, DeleteView, UpdateView
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from .models import Leads
from .forms import NewLeadForm


@login_required(login_url='staff:login')
@permission_required('crm.view_customer', raise_exception=True)
def customers_list(request: HttpRequest) -> HttpResponse:
    context = {
        "leads": Leads.objects.filter(status=False).all()
    }
    return render(request, "leads/leads-list.html", context=context)


@login_required(login_url='staff:login')
@permission_required('crm.add_customer', raise_exception=True)
def new_customer(request: HttpRequest) -> HttpResponse:
    if request.method == "POST":
        form = NewLeadForm(request.POST)
        if form.is_valid():
            Leads.objects.create(**form.cleaned_data)
            url = reverse('leads:leads')
            return redirect(url)
    else:
        form = NewLeadForm()
    context = {
        "form": form,
    }
    return render(request, 'leads/leads-create.html', context=context)


class LeadDetail(LoginRequiredMixin, PermissionRequiredMixin, DetailView):
    template_name = 'leads/leads-detail.html'
    queryset = Leads.objects.prefetch_related()
    context_object_name = 'object'
    permission_required = 'crm.view_customer'

    def get(self, request, *args, **kwargs):
        try:
            return super().get(request, *args, **kwargs)
        except Http404:
            return redirect(reverse('leads:leads'))


class LeadDelete(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    template_name = 'leads/leads-delete.html'
    queryset = Leads.objects.prefetch_related()
    context_object_name = 'object'
    success_url = reverse_lazy("leads:leads")
    permission_required = 'crm.delete_customer'

    def get(self, request, *args, **kwargs):
        try:
            return super().get(request, *args, **kwargs)
        except Http404:
            return redirect(reverse('leads:leads'))


class LeadEdit(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    model = Leads
    template_name = 'leads/leads-edit.html'
    fields = ['last_name', 'first_name', 'surname', 'phone', 'email']
    success_url = reverse_lazy("leads:leads")
    permission_required = 'crm.change_customer'

    def get(self, request, *args, **kwargs):
        try:
            return super().get(request, *args, **kwargs)
        except Http404:
            return redirect(reverse('leads:leads'))