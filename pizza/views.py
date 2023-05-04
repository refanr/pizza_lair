from django.shortcuts import render

pizzas = [
    {'name': 'margherita', 'price': 2400},
    {'name': 'pepperoni', 'price': 2700}
]

# Create your views here.

def index(request):
    return render(request, 'pizza/index.html', context={'pizzas': pizzas})