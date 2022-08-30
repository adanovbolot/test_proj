from django import forms
from .models import RegisterBuyer, RegisterProvider


class RegisterBuyerForm(forms.ModelForm):
    class Meta:
        model = RegisterBuyer
        fields = '__all__'


class RegisterProviderForm(forms.ModelForm):

    class Meta:
        model = RegisterProvider
        fields = '__all__'
