from django.shortcuts import render, redirect
from pizza.models import Pizza

# Create your views here.


# All pizzas
def index(request):#pizza_list(request):
    sort_by = request.GET.get('sort_by', 'price')
    if sort_by == 'price':
        pizzas = Pizza.objects.all().order_by('price')
    else:
        pizzas = Pizza.objects.all().order_by('name')

    if request.method == "POST":
        data = request.POST
        action = data.get("pizzaName")
        if action:
            cart = request.session.get('cart', [])
            cart.append(action)
            request.session['cart'] = cart
            return redirect('pizza-index')
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
