from django.shortcuts import render, redirect
from pizza.models import Pizza

def index(request):
    pizza = Pizza.objects.get(name='Margherita')
    discounted_price = pizza.price * 0.5 # apply a 50% discount
    context = {'pizza': pizza, 'discounted_price': discounted_price}
    if request.method == "POST":
        data = request.POST
        action = data.get("pizzaName")
        if action:
            cart = request.session.get('cart', [])
            cart.append(action)
            request.session['cart'] = cart
            return redirect('offer-index') # redirect to the offer index page
    return render(request, 'offer/index.html', context)

# All offers view
# def all_offers(request):
#     offers = Offer.objects.all()
#     return render(request, 'offer/all_offers.html', {'offers': offers})
#
# # Offer individual view
# def offer_detail(request, pk):
#     offer = get_object_or_404(Offer, pk=pk)
#     return render(request, 'myapp/offer_detail.html', {'offer': offer})