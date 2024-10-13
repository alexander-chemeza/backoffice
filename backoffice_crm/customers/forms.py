from django import forms
from leads.models import Leads
from ads.models import Ads


class NewCustomerForm(forms.Form):
    user = forms.ModelChoiceField(
        queryset=Leads.objects.filter(status=False).all(),
        widget=forms.Select(attrs={"class": "form-control"}),
        required=True,
        label='Пользователь'
    )
    advertisement = forms.ModelChoiceField(
        queryset=Ads.objects.all(),
        widget=forms.Select(attrs={"class": "form-control"}),
        required=True,
        label='Рекламная кампания'
    )