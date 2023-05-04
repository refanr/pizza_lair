from django.shortcuts import render

pizzas = [
    {'name': 'margherita', 'price': 2400, 'toppings': ['sauce', 'cheese']},
    {'name': 'pepperoni', 'price': 2700, 'toppings': ['sauce', 'cheese', 'pepperoni']}
]

# Create your views here.

def index(request):
    return render(request, 'pizza/index.html', context={'pizzas': pizzas})