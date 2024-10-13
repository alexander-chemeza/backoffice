from django.shortcuts import render, redirect, reverse
from django.http import HttpResponse, HttpRequest, Http404
from django.views.generic import DetailView, DeleteView, UpdateView
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin


from .models import Products
from .forms import NewProductForm

@login_required(login_url='staff:login')
@permission_required('products.view_products', raise_exception=True)
def services_list(request: HttpRequest) -> HttpResponse:
    context = {
        "products": Products.objects.all()
    }
    return render(request, "products/products-list.html", context=context)


@login_required(login_url='staff:login')
@permission_required('products.add_products', raise_exception=True)
def new_service(request: HttpRequest) -> HttpResponse:
    if request.method == "POST":
        form = NewProductForm(request.POST)
        if form.is_valid():
            Products.objects.create(**form.cleaned_data)
            url = reverse('products:services')
            return redirect(url)
    else:
        form = NewProductForm()
    context = {
        "form": form,
    }
    return render(request, 'products/products-create.html', context=context)


class ServiceDetail(LoginRequiredMixin, PermissionRequiredMixin, DetailView):
    template_name = 'products/products-detail.html'
    queryset = Products.objects.prefetch_related()
    context_object_name = 'object'
    permission_required = 'products.view_products'

    def get(self, request, *args, **kwargs):
        try:
            return super().get(request, *args, **kwargs)
        except Http404:
            return redirect(reverse('products:services'))


class ServiceDetele(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    template_name = 'products/products-delete.html'
    queryset = Products.objects.prefetch_related()
    context_object_name = 'object'
    success_url = reverse_lazy("products:services")
    permission_required = 'products.delete_products'

    def get(self, request, *args, **kwargs):
        try:
            return super().get(request, *args, **kwargs)
        except Http404:
            return redirect(reverse('products:services'))


class ServiceEdit(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    model = Products
    template_name = 'products/products-edit.html'
    fields = ['name', 'description', 'cost']
    success_url = reverse_lazy("products:services")
    permission_required = 'products.change_products'

    def get(self, request, *args, **kwargs):
        try:
            return super().get(request, *args, **kwargs)
        except Http404:
            return redirect(reverse('products:services'))
