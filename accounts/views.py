from django.shortcuts import render

from django.views.generic import View, TemplateView, ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy


from accounts import forms




# Create your views here.
class SignUp(CreateView):
	form_class = forms.UserCreateForm
	success_url = reverse_lazy('accounts:login')
	template_name = 'accounts/signup.html'



class userPanelView(TemplateView):
	template_name = 'accounts/userpanel.html'


