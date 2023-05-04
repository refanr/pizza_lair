from django import forms
from checkout.models import Checkout

class CheckoutForm(forms.ModelForm):
    class Meta:
        model = Checkout
        fields = ['pizzas', 'total']
        widgets = {
            'pizzas': forms.CheckboxSelectMultiple(),
            'total': forms.HiddenInput(),
        }