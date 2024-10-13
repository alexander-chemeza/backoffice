from django.shortcuts import render, redirect, reverse
from django.http import HttpResponse, HttpRequest, Http404
from django.views.generic import DetailView, DeleteView, UpdateView
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin


from .models import Ads
from .forms import NewAdvertisementForm


@login_required(login_url='staff:login')
@permission_required('ads.view_ads', raise_exception=True)
def advertisements_list(request: HttpRequest) -> HttpResponse:
    context = {
        "ads": Ads.objects.all()
    }
    return render(request, "ads/ads-list.html", context=context)


@login_required(login_url='staff:login')
@permission_required('ads.add_ads', raise_exception=True)
def new_advertisement(request: HttpRequest) -> HttpResponse:
    if request.method == "POST":
        form = NewAdvertisementForm(request.POST)
        if form.is_valid():
            Ads.objects.create(**form.cleaned_data)
            url = reverse('ads:advertisements')
            return redirect(url)
    else:
        form = NewAdvertisementForm()
    context = {
        "form": form,
    }
    return render(request, 'ads/ads-create.html', context=context)


class AdvertisementDetail(LoginRequiredMixin, PermissionRequiredMixin, DetailView):
    template_name = 'ads/ads-detail.html'
    queryset = Ads.objects.prefetch_related('service')
    context_object_name = 'object'
    permission_required = 'ads.view_ads'

    def get(self, request, *args, **kwargs):
        try:
            return super().get(request, *args, **kwargs)
        except Http404:
            return redirect(reverse('ads:advertisements'))


class AdvertisementDelete(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    template_name = 'ads/ads-delete.html'
    queryset = Ads.objects.prefetch_related('service')
    context_object_name = 'object'
    success_url = reverse_lazy("ads:advertisements")
    permission_required = 'ads.delete_ads'

    def get(self, request, *args, **kwargs):
        try:
            return super().get(request, *args, **kwargs)
        except Http404:
            return redirect(reverse('ads:advertisements'))


class AdvertisementEdit(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    model = Ads
    template_name = 'ads/ads-edit.html'
    fields = ['name', 'channel', 'budget', 'service']
    success_url = reverse_lazy("ads:advertisements")
    permission_required = 'ads.change_ads'

    def get(self, request, *args, **kwargs):
        try:
            return super().get(request, *args, **kwargs)
        except Http404:
            return redirect(reverse('ads:advertisements'))
