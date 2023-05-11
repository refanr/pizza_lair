from django import forms
from checkout.models import Checkout
from django import forms
class CheckoutForm(forms.ModelForm):
    class Meta:
        model = Checkout
        fields = ['pizzas', 'total']
        widgets = {
            'pizzas': forms.CheckboxSelectMultiple(),
            'total': forms.HiddenInput(),
        }



class PaymentForm(forms.Form):
    name = forms.CharField(max_length=100)
    address = forms.CharField(max_length=200)
    phone_number = forms.CharField(max_length=20)
    card_number = forms.CharField(max_length=16)
    exp_month = forms.CharField(max_length=2, label="Expiration Month (MM)")
    exp_year = forms.CharField(max_length=4, label="Expiration Year (YYYY)")
    cvc = forms.CharField(max_length=3)
