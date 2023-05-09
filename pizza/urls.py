from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="pizza-index"),
    path('', views.index, name='pizza_list'),
    path('<int:pizza_id>/', views.pizza_detail, name='pizza_detail')
]