from django import forms
from checkout.models import Checkout
from django import forms
from django_countries.fields import CountryField
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
    card_number = forms.CharField(max_length=16)
    exp_month = forms.CharField(max_length=2, label="Expiration Month (MM)")
    exp_year = forms.CharField(max_length=4, label="Expiration Year (YYYY)")
    cvc = forms.CharField(max_length=3)

class ContactInfoForm(forms.Form):
    name = forms.CharField(max_length=100)
    address = forms.CharField(max_length=200)
    city = forms.CharField(max_length=100)
    postal_code = forms.CharField(max_length=5)
    country = CountryField(blank_label="Please select country").formfield()
