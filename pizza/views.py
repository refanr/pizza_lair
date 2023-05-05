from django.shortcuts import render, get_object_or_404
from pizza.models import Pizza

# Create your views here.

def index(request):
    return render(request, 'pizza/index.html')

# All pizzas
def pizza_list(request):
    pizzas = Pizza.objects.all()
    return render(request, 'pizza/pizza_list.html', {'pizzas': pizzas})


# Individual pizza object
def pizza_detail(request, pk):
    pizza = get_object_or_404(Pizza, pk=pk)
    return render(request, 'pizza/pizza_detail.html', {'pizza': pizza})
