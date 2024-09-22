from django import forms
from .models import Advertisements, Services, Customer


class NewServiceForm(forms.Form):
    name = forms.CharField(max_length=300, label="Название продукта")
    description = forms.CharField(widget=forms.Textarea(attrs={"rows":"5"}), label="Описание")
    cost = forms.DecimalField(max_digits=10, decimal_places=2, label="Цена")


class NewAdvertisementForm(forms.Form):
    name = forms.CharField(max_length=300, label="Название рекламной кампании")
    channel = forms.CharField(max_length=300, label="Название канала продвижения")
    budget = forms.DecimalField(max_digits=10, decimal_places=2, label="Бюджет на рекламу")
    service = forms.ModelChoiceField(
        queryset=Services.objects.all(),
        widget=forms.Select(attrs={"class":"form-control"}),
        required=True,
        label='Услуга',
        to_field_name='name',
    )


class NewCustomerForm(forms.Form):
    last_name = forms.CharField(max_length=200, label="Фамилия")
    first_name = forms.CharField(max_length=200, label="Имя")
    surname = forms.CharField(max_length=200, label="Отчество")
    phone = forms.CharField(max_length=200, label="Телефон")
    email = forms.EmailField(max_length=300, label="Email")


class NewActiveCustomerForm(forms.Form):
    user = forms.ModelChoiceField(
        queryset=Customer.objects.filter(status=False).all(),
        widget=forms.Select(attrs={"class": "form-control"}),
        required=True,
        label='Пользователь'
    )
    advertisement = forms.ModelChoiceField(
        queryset=Advertisements.objects.all(),
        widget=forms.Select(attrs={"class": "form-control"}),
        required=True,
        label='Рекламная кампания'
    )


class NewContractForm(forms.Form):
    name = forms.CharField(max_length=300, label="Название контракта")
    service = forms.ModelChoiceField(
        queryset=Services.objects.all(),
        widget=forms.Select(attrs={"class": "form-control"}),
        required=True,
        label='Услуга'
    )
    file = forms.FileField(widget=forms.ClearableFileInput(attrs={"class":"form-control"}), label="Файл")
    contract_date = forms.DateField(widget=forms.DateInput(attrs={"class":"form-control", "type": "date"}), label="Дата заключения контракта")
    period = forms.DateField(widget=forms.DateInput(attrs={"class":"form-control", "type": "date"}), label="Дата окончания контракта")
    total_cost = forms.DecimalField(max_digits=10, decimal_places=2, label="Полная стоимость")
    user = forms.ModelChoiceField(
        queryset=Customer.objects.all(),
        widget=forms.Select(attrs={"class": "form-control"}),
        required=True,
        label='Пользователь'
    )