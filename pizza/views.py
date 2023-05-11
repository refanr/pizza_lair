from django.http import JsonResponse
from django.shortcuts import render, redirect
from pizza.models import Pizza

# Create your views here.


# All pizzas
def index(request):#pizza_list(request):

    if 'search_filter' in request.GET:
      search_filter = request.GET['search_filter']
      pizzas = [{
          'id':  x.id,
          'name': x.name,
          'description': x.description,
          'price': x.price,
          'toppings': x.toppings.order_by('name')
      } for x in Pizza.objects.filter(name__icontains=search_filter) ]
      return JsonResponse({'data':pizzas})
    if request.method == "POST":
        data = request.POST
        action = data.get("pizzaName")
        if action:
            cart = request.session.get('cart', [])
            cart.append(action)
            request.session['cart'] = cart
            return redirect('pizza-index')
    pizzas = Pizza.objects.all().order_by('name')
    return render(request, 'pizza/index.html', {'pizzas': pizzas})

# views.py

def pizza_detail(request, pizza_id):
    pizza = Pizza.objects.get(id=pizza_id)
    context = {'pizza': pizza}
    return render(request, 'pizza/pizza_detail.html', context)



# Individual pizza object
# def pizza_detail(request, pk):
#     pizza = get_object_or_404(Pizza, pk=pk)
#     return render(request, 'pizza/pizza_detail.html', {'pizza': pizza})
