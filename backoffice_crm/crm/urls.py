from django.urls import path
from django.views.generic import TemplateView

app_name = 'crm'

urlpatterns = [
    path('', TemplateView.as_view(template_name='crm/users/index.html'),),
    path('login/', TemplateView.as_view(template_name='crm/registration/login.html'),),
    path('products-create/', TemplateView.as_view(template_name='crm/products/products-create.html'),),
    path('products-delete/<int:id>/', TemplateView.as_view(template_name='crm/products/products-delete.html'),),
    path('products-detail/<int:id>/', TemplateView.as_view(template_name='crm/products/products-detail.html'),),
    path('products-edit/<int:id>/', TemplateView.as_view(template_name='crm/products/products-edit.html'),),
    path('products/', TemplateView.as_view(template_name='crm/products/products-list.html'),),
    path('leads-create/', TemplateView.as_view(template_name='crm/leads/leads-create.html'),),
    path('leads-delete/<int:id>/', TemplateView.as_view(template_name='crm/leads/leads-delete.html'),),
    path('leads-detail/<int:id>/', TemplateView.as_view(template_name='crm/leads/leads-detail.html'),),
    path('leads-edit/<int:id>/', TemplateView.as_view(template_name='crm/leads/leads-edit.html'),),
    path('leads/', TemplateView.as_view(template_name='crm/leads/leads-list.html'),),
    path('customers-create/', TemplateView.as_view(template_name='crm/customers/customers-create.html'),),
    path('customers-delete/<int:id>/', TemplateView.as_view(template_name='crm/customers/customers-delete.html'),),
    path('customers-detail/<int:id>/', TemplateView.as_view(template_name='crm/customers/customers-detail.html'),),
    path('customers-edit/<int:id>/', TemplateView.as_view(template_name='crm/customers/customers-edit.html'),),
    path('customers/', TemplateView.as_view(template_name='crm/customers/customers-list.html'),),
    path('contracts-create/', TemplateView.as_view(template_name='crm/contracts/contracts-create.html'),),
    path('contracts-delete/<int:id>/', TemplateView.as_view(template_name='crm/contracts/contracts-delete.html'),),
    path('contracts-detail/<int:id>/', TemplateView.as_view(template_name='crm/contracts/contracts-detail.html'),),
    path('contracts-edit/<int:id>/', TemplateView.as_view(template_name='crm/contracts/contracts-edit.html'),),
    path('contracts/', TemplateView.as_view(template_name='crm/contracts/contracts-list.html'),),
    path('ads-create/', TemplateView.as_view(template_name='crm/ads/ads-create.html'),),
    path('ads-delete/<int:id>/', TemplateView.as_view(template_name='crm/ads/ads-delete.html'),),
    path('ads-detail/<int:id>/', TemplateView.as_view(template_name='crm/ads/ads-detail.html'),),
    path('ads-edit/<int:id>/', TemplateView.as_view(template_name='crm/ads/ads-edit.html'),),
    path('ads-list/', TemplateView.as_view(template_name='crm/ads/ads-list.html'),),
    path('ads/', TemplateView.as_view(template_name='crm/ads/ads-statistic.html'),),
]