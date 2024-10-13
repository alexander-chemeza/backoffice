from django.urls import path
from .views import (
    new_contract,
    contracts_list,
    ContractDetail,
    ContractDelete,
    ContractEdit,
)

app_name = 'contracts'

urlpatterns = [
    path('contracts/', contracts_list, name='contracts'),
    path('contracts/new/', new_contract, name='new_contract'),
    path('contracts/<int:pk>/delete/', ContractDelete.as_view(), name='delete_contract'),
    path('contracts/<int:pk>/', ContractDetail.as_view(), name='contract_details'),
    path('contracts/<int:pk>/edit/', ContractEdit.as_view(), name="edit_contract"),
]