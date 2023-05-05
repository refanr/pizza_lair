from django.urls import path
from .views import all_offers, offer_detail

app_name = 'offer'

urlpatterns = [
    path('', all_offers, name='all_offers'),
    path('<int:pk>/', offer_detail, name='offer_detail'),
]
