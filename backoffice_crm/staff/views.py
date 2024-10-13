from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpRequest
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from products.models import Products
from ads.models import Ads
from leads.models import Leads
from customers.models import Customers


def logout_view(request: HttpRequest):
    logout(request)
    return redirect("staff:login")


@login_required(login_url="staff:login")
def home_view(request: HttpRequest) -> HttpResponse:
    context = {
        "products_count": Products.objects.all().count(),
        "advertisements_count": Ads.objects.all().count(),
        "leads_count": Leads.objects.filter(status=False).all().count(),
        "customers_count": Customers.objects.all().count(),
    }
    return render(request, "staff/index.html", context=context)