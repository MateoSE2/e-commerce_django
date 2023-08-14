from django.shortcuts import render

from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic

### To use custom html templates (Not created) ###

class SignUp(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'

# from django.contrib.auth.views import LoginView, LogoutView

# class UserLoginView(LoginView):
#     template_name = 'registration/login.html'

# class UserLogoutView(LogoutView):
#     template_name = 'registration/logout.html'

from django.views import generic
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

class LandingPageView(generic.TemplateView):
    template_name = 'landing_page.html'

@method_decorator(login_required, name='dispatch')
class UserPageView(generic.TemplateView):
    template_name = 'user_page.html'
