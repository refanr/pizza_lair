from django.shortcuts import render
from .models import Offer


# Create your views here.

# All offers view
def all_offers(request):
    offers = Offer.objects.all()
    return render(request, 'offer/all_offers.html', {'offers': offers})

# Offer individual view
def offer_detail(request, pk):
    offer = get_object_or_404(Offer, pk=pk)
    return render(request, 'myapp/offer_detail.html', {'offer': offer})