from django.shortcuts import render, redirect
from django.conf import settings

from .forms import SignupForm

def signup(request):
  template_name = 'accounts/signup.html'
  if request.method == "POST":
    form = SignupForm(request.POST)
    if form.is_valid():
      form.save()
      return redirect(settings.LOGIN_URL)
  else:
    form = SignupForm()

  context = {
    'form': form
  }

  return render(request, template_name, context)
