from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect

from user.forms.custom_user_creation_form import CustomUserCreationForm
from user.forms.profile_form import ProfileForm
from user.models import Profile


# Create your views here.

def register(request):
  if request.method == 'POST':
    form = CustomUserCreationForm(data=request.POST)

    if form.is_valid():
      form.save()
      return redirect('login')
  return render(request, 'user/register.html', {
    'form': CustomUserCreationForm()
  })

def profile(request):
  profile = Profile.objects.filter(user=request.user).first()
  if request.method == 'POST':
    form = ProfileForm(instance=profile, data=request.POST)
    if form.is_valid():
      profile = form.save(commit=False)
      profile.user = request.user
      profile.save()
      return redirect('profile')
  return render(request, 'user/profile.html', {
    'form': ProfileForm(instance=profile)
  })