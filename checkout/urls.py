from django.urls import path
from .views import checkout, checkout_history

app_name = 'checkout'

urlpatterns = [
    path('', checkout, name='checkout'),
    path('history/', checkout_history, name='checkout_history'),
]