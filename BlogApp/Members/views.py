from django.shortcuts import render
from django.views import generic
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy

# from django.contrib.auth.views import LogoutView


class CreateUserForm(generic.CreateView):
    form_class = UserCreationForm
    template_name = 'registration/create_user.html'
    success_url = reverse_lazy('login')


# class Logout(LogoutView):
#     template_name = 'registration/logout.html'
#     # success_url = reverse_lazy('login')














