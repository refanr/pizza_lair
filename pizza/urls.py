from django.urls import path
from .views import index, pizza_list, pizza_detail

app_name = 'pizza'

urlpatterns = [
    path('', index, name="index"),
    path('pizzas/', pizza_list, name='pizza_list'),
    path('pizzas/<int:pk>/', pizza_detail, name='pizza_detail'),
]