from django.shortcuts import render, redirect
from pizza.models import Pizza
# from checkout.models import Checkout
# from checkout.forms import CheckoutForm

# Checkout views..

def index(request):
  cart = request.session.get('cart', [])
  pizza_names = list(set(cart))  # Get unique pizza names from the cart
  pizzas = Pizza.objects.filter(name__in=pizza_names)
  total_price = 0

  for pizza in pizzas:
    quantity = cart.count(pizza.name)  # Get the quantity of the pizza from the cart
    if pizza.name == 'Margherita':
      pizza.price *= 0.5  # Apply discount to Margherita pizza
    total_price += pizza.price * quantity  # Multiply price by quantity

  return render(request, 'checkout/index.html', {'pizzas': pizzas, 'total_price': total_price})

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
