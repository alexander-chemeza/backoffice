from django import forms
from products.models import Products
from customers.models import Customers


class NewContractForm(forms.Form):
    name = forms.CharField(max_length=300, label="Название контракта")
    service = forms.ModelChoiceField(
        queryset=Products.objects.all(),
        widget=forms.Select(attrs={"class": "form-control"}),
        required=True,
        label='Услуга'
    )
    file = forms.FileField(widget=forms.ClearableFileInput(attrs={"class":"form-control"}), label="Файл")
    contract_date = forms.DateField(widget=forms.DateInput(attrs={"class":"form-control", "type": "date"}), label="Дата заключения контракта")
    period = forms.DateField(widget=forms.DateInput(attrs={"class":"form-control", "type": "date"}), label="Дата окончания контракта")
    total_cost = forms.DecimalField(max_digits=10, decimal_places=2, label="Полная стоимость")
    user = forms.ModelChoiceField(
        queryset=Customers.objects.all(),
        widget=forms.Select(attrs={"class": "form-control"}),
        required=True,
        label='Пользователь'
    )