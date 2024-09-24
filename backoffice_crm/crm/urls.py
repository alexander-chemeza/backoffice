from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path
from django.views.generic import TemplateView

from .views import (
    new_service,
    new_advertisement,
    new_customer,
    new_contract,
    new_active_customer,
    services_list,
    advertisements_list,
    customers_list,
    customers_active_list,
    contracts_list,
    ServiceDetail,
    AdvertisementDetail,
    LeadDetail,
    CustomerDetail,
    ContractDetail,
    ServiceDetele,
    AdvertisementDelete,
    LeadDelete,
    CustomerDelete,
    ContractDelete,
    ServiceEdit,
    AdvertisementEdit,
    LeadEdit,
    CustomerEdit,
    ContractEdit,
    logout_view,
    home_view,
)

app_name = 'crm'

urlpatterns = [
    # START OF TEMPLATES ROUTES

    # Main pages
    path('', home_view, name='home'),
    path(
        'login/',
        LoginView.as_view(
            template_name='crm/registration/login.html',
            redirect_authenticated_user=True,
        ),
        name='login'
    ),
    path('accounts/logout/', logout_view, name='logout'),

    # Listings
    path('products/', services_list, name='services'),
    path('leads/', customers_list, name='leads'),
    path('customers/', customers_active_list, name='customers'),
    path('contracts/', contracts_list, name='contracts'),
    path('ads/', advertisements_list, name='advertisements'),

    # New instances
    path('products/new/', new_service, name='new_service'),
    path('leads/new/', new_customer, name='new_customer'),
    path('customers/new/', new_active_customer, name='new_active_customer'),
    path('contracts/new/', new_contract, name='new_contract'),
    path('ads/new/', new_advertisement, name='new_advertisement'),

    # Delete instances
    path('products/<int:pk>/delete/', ServiceDetele.as_view(), name='delete_service'),
    path('leads/<int:pk>/delete/', LeadDelete.as_view(), name='delete_lead'),
    path('customers/<int:pk>/delete/', CustomerDelete.as_view(), name='delete_customer'),
    path('contracts/<int:pk>/delete/', ContractDelete.as_view(), name='delete_contract'),
    path('ads/<int:pk>/delete/', AdvertisementDelete.as_view(), name='delete_advertisement'),

    # Instance details
    path('products/<int:pk>/', ServiceDetail.as_view(), name='service_details'),
    path('leads/<int:pk>/', LeadDetail.as_view(), name='lead_details'),
    path('customers/<int:pk>/', CustomerDetail.as_view(), name='customer_details'),
    path('contracts/<int:pk>/', ContractDetail.as_view(), name='contract_details'),
    path('ads/<int:pk>/', AdvertisementDetail.as_view(), name='ad_details'),
    path('ads/statistic/', TemplateView.as_view(template_name='crm/ads/ads-statistic.html'),),

    # Instance edit
    path('products/<int:pk>/edit/', ServiceEdit.as_view(), name='edit_service'),
    path('leads/<int:pk>/edit/', LeadEdit.as_view(), name='edit_lead'),
    path('customers/<int:pk>/edit/', CustomerEdit.as_view(), name="edit_customer"),
    path('contracts/<int:pk>/edit/', ContractEdit.as_view(), name="edit_contract"),
    path('ads/<int:pk>/edit/', AdvertisementEdit.as_view(), name='edit_advertisement'),

    # END OF TEMPLATES ROUTES
]