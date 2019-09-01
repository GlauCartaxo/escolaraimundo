from django.shortcuts import render
from users.models import Usuario
from django.views import generic
from django.views.generic import DetailView
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy 
# Create your views here.


class UserLoginView(LoginView):
    template_name = 'users/login.html'

class UserLogoutView(LoginRequiredMixin, LogoutView):
    pass

class UserDetailView(DetailView):
    model = Usuario
    template_name = "users/detail.html"
    context_object_name = 'users'

