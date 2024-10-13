from django.urls import path
from .views import (
    new_service,
    services_list,
    ServiceDetail,
    ServiceDetele,
    ServiceEdit,
)

app_name = 'products'

urlpatterns = [
    path('products/', services_list, name='services'),
    path('products/new/', new_service, name='new_service'),
    path('products/<int:pk>/delete/', ServiceDetele.as_view(), name='delete_service'),
    path('products/<int:pk>/', ServiceDetail.as_view(), name='service_details'),
    path('products/<int:pk>/edit/', ServiceEdit.as_view(), name='edit_service'),
]