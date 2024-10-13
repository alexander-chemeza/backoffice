from django.urls import path

from .views import (
    new_active_customer,
    customers_active_list,
    CustomerDetail,
    CustomerDelete,
    CustomerEdit,
)

app_name = 'customers'

urlpatterns = [
    path('customers/', customers_active_list, name='customers'),
    path('customers/new/', new_active_customer, name='new_active_customer'),
    path('customers/<int:pk>/delete/', CustomerDelete.as_view(), name='delete_customer'),
    path('customers/<int:pk>/', CustomerDetail.as_view(), name='customer_details'),
    path('customers/<int:pk>/edit/', CustomerEdit.as_view(), name="edit_customer"),
]