from django.shortcuts import render, redirect
from pizza.models import Pizza
# from checkout.models import Checkout
# from checkout.forms import CheckoutForm

# Checkout views..
def index(request):
  cart = request.session.get('cart', [])
  pizza_names = list(set(cart))
  pizzas = Pizza.objects.filter(name__in=pizza_names)
  total_price = 0
  pizza_counts = {}  # Dictionary to store the quantity of each pizza

  for pizza in pizzas:
    quantity = cart.count(pizza.name)
    if pizza.name == 'Margherita':
      pizza.price *= 0.5
    total_price += pizza.price * quantity
    pizza_counts[pizza.name] = quantity  # Add pizza name and quantity to dictionary

  context = {
    'pizzas': pizzas,
    'total_price': total_price,
    'pizza_counts': pizza_counts  # Include 'pizza_counts' in the context
  }
  return render(request, 'checkout/index.html', context)

#checkout history view
# def checkout_history(request):
#     checkouts = Checkout.objects.filter(user=request.user).order_by('-date')
#     return render(request, 'checkout_history.html', {'checkouts': checkouts})
#
# #Viewið hér að neðan být til nýjan checkout obj þegar user er búinn að velja pizzur og ýtir á checkout takkann
# #og vistar checkout obj í gagnagrunninn og reiknar út heildarverð pöntunarinnar
# def checkout(request):
#     if request.method == 'POST':
#         checkout = form.save(commit=False)
#         checkout.user = request.user
#         checkout.total = sum([pizza.price for pizza in checkout.pizzas.all()])
#         checkout.save()
#         form.save_m2m() # vista pizzurnar í pöntuninni
#         return redirect('checkout_complete')
#     else:
#         form = CheckoutForm()
#         return render(request, 'checkout.html', {'form': form})
