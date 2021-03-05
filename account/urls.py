from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from django.views.generic import TemplateView
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy

from .views import UserRegistrationView



urlpatterns = [
	path('register/', UserRegistrationView.as_view(), name='register'),
	path('login/', LoginView.as_view(redirect_authenticated_user=True), name='login'),
	path('logout/', LogoutView.as_view(), name='logout'),

	path('home/', login_required(
    	TemplateView.as_view(template_name = 'home.html'), 
    	login_url=reverse_lazy('login'))
    )
]