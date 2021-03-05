from django.shortcuts import render
from django.views.generic import CreateView
from django.urls import reverse_lazy
from django.contrib.auth.forms import UserCreationForm


class UserRegistrationView(CreateView):
	template_name = 'registration/register.html'
	success_url = reverse_lazy('login')
	form_class = UserCreationForm