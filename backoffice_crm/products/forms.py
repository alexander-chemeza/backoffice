from django import forms


class NewProductForm(forms.Form):
    name = forms.CharField(max_length=300, label="Название продукта")
    description = forms.CharField(widget=forms.Textarea(attrs={"rows":"5"}), label="Описание")
    cost = forms.DecimalField(max_digits=10, decimal_places=2, label="Цена")