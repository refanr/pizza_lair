from django.shortcuts import render
from pizza.models import Pizza

# Create your views here.


# All pizzas
def pizza_list(request):
    pizzas = Pizza.objects.all()
    return render(request, 'pizza/pizza_list.html', {'pizzas': pizzas})


# Individual pizza object
def pizza_detail(request, pk):
    pizza = Pizza.objects.get(pk=pk)
    return render(request, 'pizza/pizza_detail.html', {'pizza': pizza})
