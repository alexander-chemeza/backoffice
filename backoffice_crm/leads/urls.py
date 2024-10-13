from django.urls import path
from .views import (
    new_customer,
    customers_list,
    LeadDetail,
    LeadDelete,
    LeadEdit,
)

app_name = 'leads'

urlpatterns = [
    path('leads/', customers_list, name='leads'),
    path('leads/new/', new_customer, name='new_customer'),
    path('leads/<int:pk>/delete/', LeadDelete.as_view(), name='delete_lead'),
    path('leads/<int:pk>/', LeadDetail.as_view(), name='lead_details'),
    path('leads/<int:pk>/edit/', LeadEdit.as_view(), name='edit_lead'),
]