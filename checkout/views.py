from django.shortcuts import render, redirect
from pizza.models import Pizza
# from checkout.models import Checkout
# from checkout.forms import CheckoutForm
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import datetime
from .forms import PaymentForm, ContactInfoForm

# ...

@csrf_exempt  # This is needed to allow POST requests
def add_pizza(request, pizza_id):
    cart = request.session.get('cart', [])
    pizza = Pizza.objects.get(id=pizza_id)
    cart.append(pizza.name)
    request.session['cart'] = cart
    return JsonResponse({'status': 'ok'})

@csrf_exempt  # This is needed to allow POST requests
def remove_pizza(request, pizza_id):
    cart = request.session.get('cart', [])
    pizza = Pizza.objects.get(id=pizza_id)
    if pizza.name in cart:
        cart.remove(pizza.name)
        request.session['cart'] = cart
    return JsonResponse({'status': 'ok'})

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

def payment_options(request):
    cart = request.session.get('cart', [])
    pizza_names = list(set(cart))
    pizzas = Pizza.objects.filter(name__in=pizza_names)
    total_price = 0

    for pizza in pizzas:
        quantity = cart.count(pizza.name)
        if pizza.name == 'Margherita':
            pizza.price *= 0.5
        total_price += pizza.price * quantity

    return render(request, 'checkout/payment_options.html', {'total_price': total_price})

def get_pizza(request):
    pickup_time = datetime.datetime.now() + datetime.timedelta(minutes=15)
    return render(request, 'checkout/get_pizza.html', {'pickup_time': pickup_time})


def info_form(request):
    form = ContactInfoForm()
    return render(request, 'checkout/info_form.html', {'form': form})

def cc_form(request):
    form = PaymentForm()
    return render(request, 'checkout/cc_form.html', {'form': form})

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
