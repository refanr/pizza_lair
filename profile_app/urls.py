from django.urls import path
from .views import user_profile, all_users

app_name = 'profile_app'

urlpatterns = [
    path('', all_users, name='all_users'),
    path('<int:pk>/', user_profile, name='user_profile'),
]