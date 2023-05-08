from django.shortcuts import render
from pizza.models import Pizza
# from .models import Offer


# Create your views here.

# Pizza of the week offer.

#Pizza vikunar eeeeeeer MARGHARITA (erum að spara álegg)
def index(request):
  pizza = Pizza.objects.get(name='Margherita')
  discounted_price = pizza.price * 0.5
  return render(request, 'offer/index.html', {'pizza': pizza, 'discounted_price': discounted_price})
# All offers view
# def all_offers(request):
#     offers = Offer.objects.all()
#     return render(request, 'offer/all_offers.html', {'offers': offers})
#
# # Offer individual view
# def offer_detail(request, pk):
#     offer = get_object_or_404(Offer, pk=pk)
#     return render(request, 'myapp/offer_detail.html', {'offer': offer})