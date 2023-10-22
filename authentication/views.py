from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.decorators import login_required
from django.views.generic.edit import CreateView
from django.http import HttpResponse
from django.contrib.auth.models import User
from .forms import CustomUserForm

from django.shortcuts import redirect



class UserCreationFormView(CreateView):
    template_name = 'auth/sign-up.html'
    model = User
    form_class = UserCreationForm
    success_url = 'sign-in-page'

    def get_queryset(self):
        return super().get_queryset()
    

class UserLoginView(LoginView):
    template_name = 'auth/sign-in.html'
    success_url = 'private-page'


class UserLogoutView(LogoutView):
    template_name = 'auth/sign-out.html'

