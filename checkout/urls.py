from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="checkout-index"),
    path('add_pizza/<int:pizza_id>/', views.add_pizza, name='add_pizza'),
    path('remove_pizza/<int:pizza_id>/', views.remove_pizza, name='remove_pizza'),
]