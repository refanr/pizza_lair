from django.shortcuts import render
# from profile_app.models import user_profile

# Create your views here.

def index(request):
  return render(request, 'profile_app/index.html')
# Individual user profile view.. Þetta ætti að virka
# fyrir profileinn hja þeim sem er logged in.
# def user_profile(request):
#     profile = user_profile.objects.get(user=request.user)
#     return render(request, 'profile_app/user_profile.html', {'profile': profile})
#
# # All users view
# def all_users(request):
#     users = user_profile.objects.all()
#     return render(request, 'profile_app/all_users.html', {'users': users})
