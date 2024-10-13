from django.urls import path
from django.views.generic import TemplateView

from .views import (
    new_advertisement,
    advertisements_list,
    AdvertisementDetail,
    AdvertisementDelete,
    AdvertisementEdit,
)

app_name = 'ads'

urlpatterns = [
    path('ads/', advertisements_list, name='advertisements'),
    path('ads/new/', new_advertisement, name='new_advertisement'),
    path('ads/<int:pk>/delete/', AdvertisementDelete.as_view(), name='delete_advertisement'),
    path('ads/<int:pk>/', AdvertisementDetail.as_view(), name='ad_details'),
    path('ads/statistic/', TemplateView.as_view(template_name='crm/ads/ads-statistic.html'),),
    path('ads/<int:pk>/edit/', AdvertisementEdit.as_view(), name='edit_advertisement'),
]