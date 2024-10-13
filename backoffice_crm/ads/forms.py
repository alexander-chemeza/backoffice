from django import forms
from products.models import Products


class NewAdvertisementForm(forms.Form):
    name = forms.CharField(max_length=300, label="Название рекламной кампании")
    channel = forms.CharField(max_length=300, label="Название канала продвижения")
    budget = forms.DecimalField(max_digits=10, decimal_places=2, label="Бюджет на рекламу")
    service = forms.ModelChoiceField(
        queryset=Products.objects.all(),
        widget=forms.Select(attrs={"class":"form-control"}),
        required=True,
        label='Услуга',
        to_field_name='name',
    )