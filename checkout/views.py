from django.shortcuts import render
# from checkout.models import Checkout
# from checkout.forms import CheckoutForm

# Checkout views..

def index(request):
  return render(request, 'checkout/index.html')

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
