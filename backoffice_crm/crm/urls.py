from django.urls import path
from django.views.generic import TemplateView

from .views import new_service, new_advertisement, new_customer, new_contract, new_active_customer

app_name = 'crm'

urlpatterns = [
    # START OF TEMPLATES ROUTES

    # Main pages
    path('', TemplateView.as_view(template_name='crm/users/index.html'),),
    path('login/', TemplateView.as_view(template_name='crm/registration/login.html'),),

    # Listings
    path('products/', TemplateView.as_view(template_name='crm/products/products-list.html'),),
    path('leads/', TemplateView.as_view(template_name='crm/leads/leads-list.html'),),
    path('customers/', TemplateView.as_view(template_name='crm/customers/customers-list.html'),),
    path('contracts/', TemplateView.as_view(template_name='crm/contracts/contracts-list.html'),),
    path('ads/', TemplateView.as_view(template_name='crm/ads/ads-list.html'),),

    # New instances
    path('products/new/', new_service, name='new_service'),
    path('leads/new/', new_customer, name='new_customer'),
    path('customers/new/', new_active_customer, name='new_active_customer'),
    path('contracts/new/', new_contract, name='new_contract'),
    path('ads/new/', new_advertisement, name='new_advertisement'),

    # Delete instances
    path('products/<int:pk>/delete/', TemplateView.as_view(template_name='crm/products/products-delete.html'),),
    path('leads/<int:pk>/delete/', TemplateView.as_view(template_name='crm/leads/leads-delete.html'),),
    path('customers/<int:pk>/delete/', TemplateView.as_view(template_name='crm/customers/customers-delete.html'),),
    path('contracts/<int:pk>/delete/', TemplateView.as_view(template_name='crm/contracts/contracts-delete.html'),),
    path('ads/<int:pk>/delete/', TemplateView.as_view(template_name='crm/ads/ads-delete.html'),),

    # Instance details
    path('products/<int:pk>/', TemplateView.as_view(template_name='crm/products/products-detail.html'),),
    path('leads/<int:pk>/', TemplateView.as_view(template_name='crm/leads/leads-detail.html'),),
    path('customers/<int:pk>/', TemplateView.as_view(template_name='crm/customers/customers-detail.html'),),
    path('contracts/<int:pk>/', TemplateView.as_view(template_name='crm/contracts/contracts-detail.html'),),
    path('ads/<int:pk>/', TemplateView.as_view(template_name='crm/ads/ads-detail.html'),),
    path('ads/statistic/', TemplateView.as_view(template_name='crm/ads/ads-statistic.html'),),

    # Instance edit
    path('products/<int:pk>/edit/', TemplateView.as_view(template_name='crm/products/products-edit.html'),),
    path('leads/<int:pk>/edit/', TemplateView.as_view(template_name='crm/leads/leads-edit.html'),),
    path('customers/<int:pk>/edit/', TemplateView.as_view(template_name='crm/customers/customers-edit.html'),),
    path('contracts/<int:pk>/edit/', TemplateView.as_view(template_name='crm/contracts/contracts-edit.html'),),
    path('ads/<int:pk>/edit/', TemplateView.as_view(template_name='crm/ads/ads-edit.html'),),

    # END OF TEMPLATES ROUTES
]