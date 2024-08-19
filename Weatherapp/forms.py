from django import forms


class MyForm(forms.Form):
    city = forms.CharField(max_length=100)