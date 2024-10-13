from django import forms


class NewLeadForm(forms.Form):
    last_name = forms.CharField(max_length=200, label="Фамилия")
    first_name = forms.CharField(max_length=200, label="Имя")
    surname = forms.CharField(max_length=200, label="Отчество")
    phone = forms.CharField(max_length=200, label="Телефон")
    email = forms.EmailField(max_length=300, label="Email")